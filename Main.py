import pandas as pd
import time
from rich.console import Console
from rich.traceback import install
install()
from loguru import logger
global console
console = Console()

console.log("[bold green][Task] [white]Loading All Resources...")
from Logger import add_logger
from Scraper import CustomGNews
from LoadConfig import *
from CloudFlare import Summarizer
import ContentTranslator
from ProxySetup import *
from FuzzyMerge import *
from LabelData import *
from TopicsClassifier import *
from EntityRecognizer import *

def _1_scraping(
        language: str = scraper_config['language'], 
        country: str = scraper_config['country'], 
        topic: str = scraper_config['topic'],
        start_date: tuple[int] = scraper_config['start_date'], 
        end_date: tuple[int] = scraper_config['end_date'],
        raw_file_path: str = file_path['file_raw_data'],
        raw_file_name: str = file_name['file_raw']
    ) -> None:
    
    google_news = CustomGNews(
        language = language, 
        country = country, 
        start_date = start_date, 
        end_date = end_date,max_results=2   
    )
    
    news = google_news.get_news_by_topic(topic) 
    news.to_excel(raw_file_path + raw_file_name, 
                  index = False)

def _2_translate(
        for_final = False,
        vercel_domain: str =vercel['google_translate'] ,
        source: str = translate_config['source'], 
        target: str = translate_config['target'],
        raw_file_path: str = file_path['file_raw_data'],
        raw_file_name: str = file_name['file_raw'],
        translate_to_en_file_path = file_path['file_translated'],
        translate_to_en_file_name = file_name['file_translated'],
        summarized_file_path: str = file_path['file_summarized'],
        summarized_file_name: str = file_name['file_summarized']
    ) -> None:

    if for_final:
        enable_proxy()
        summarized_df = pd.read_excel(summarized_file_path + summarized_file_name)
        google_translate = ContentTranslator.GoogleTranslate(summarized_df[['summarized_en']], vercel_domain, 'en', 'id')
        translated_text = google_translate.translated_text_list
        
        if len(translated_text) == summarized_df.shape[0]:
            summarized_df['summarized'] = translated_text
        else:
            translated = pd.DataFrame({
                'summarized' : translated_text
            })
            translated.reset_index(inplace = True)
            summarized_df.reset_index(drop = True, inplace = True)
            summarized_df.reset_index(inplace = True)
            summarized_df.merge(translated, left_on = 'index', right_on = 'index')
            summarized_df.drop(['index'], axis = 1, inplace = True)
            summarized_df.dropna(inplace = True)
        summarized_df.to_excel(summarized_file_path + summarized_file_name, index = False)
        disable_proxy()

    else:
        enable_proxy()
        raw_file = pd.read_excel(raw_file_path + raw_file_name)
        google_translate = ContentTranslator.GoogleTranslate(raw_file[['cleaned']], vercel_domain, 'id', 'en')
        translated_text = google_translate.translated_text_list
        
        translated_df = raw_file.copy()
        if len(translated_text) == raw_file.shape[0]:
            translated_df['translated_content'] = translated_text
        else:
            translated = pd.DataFrame({
                'translated_content' : translated_text
            })
            translated.reset_index(inplace = True)
            translated_df.reset_index(drop = True, inplace = True)
            translated_df.reset_index(inplace = True)
            translated_df.merge(translated, left_on = 'index', right_on = 'index')
            translated_df.drop(['index'], axis = 1, inplace = True)
            translated_df.dropna(inplace = True)
        translated_df.to_excel(translate_to_en_file_path + translate_to_en_file_name, index = False)
        disable_proxy()  
        
def _3_summarize(   
        vercel_key: str = vercel['gemini'],
        cloudflare_api: str = cloudfare_config['api'],
        cloudflare_user_id: str = cloudfare_config['user_id'],
        cloudflare_model: str = cloudfare_config['model'],
        translated_df_file_path = file_path['file_translated'],
        translated_df_file_name = file_name['file_translated'],
        summarized_file_path: str = file_path['file_summarized'],
        summarized_file_name: str = file_name['file_summarized']
    ) -> None:

    # translated_df = pd.read_excel(translated_df_file_path + translated_df_file_name)
    # enable_proxy()
    # summarizer = Summarizer(vercel_key, 
    #                         cloudflare_api, 
    #                         cloudflare_user_id, 
    #                         cloudflare_model, 
    #                         translated_df[['translated_content']])
    # summarized_file = translated_df.copy()
    # if len(summarizer.summarized_text_list) == summarized_file.shape[0]:
    #     summarized_file['summarized_en'] = summarizer.summarized_text_list
    # else:
    #     list_of_summarized = pd.DataFrame({
    #         'summarized_en' : summarizer.summarized_text_list
    #     })
    #     list_of_summarized.reset_index(inplace = True)
    #     summarized_file.reset_index(drop = True,inplace = True)
    #     summarized_file.reset_index(inplace = True)
    #     summarized_file = summarized_file.merge(list_of_summarized, left_on = 'index', right_on = 'index')
    #     summarized_file.drop(['index'], axis = 1, inplace = True)
    #     summarized_file.dropna(inplace = True)
    # disable_proxy()
    # summarized_file.to_excel(summarized_file_path + summarized_file_name, index = False)

    # time.sleep(1)
    _2_translate(for_final = True)

def _4_sentiment_labeling(
        summarized_file_path: str = file_path['file_summarized'],
        summarized_file_name: str = file_name['file_summarized'],
        sentiment_file_path: str = file_path['sentiment_labelled'],
        sentiment_file_name: str = file_name['sentiment_labelled']
    ) -> None:
    df = pd.read_excel(summarized_file_path + summarized_file_name)
    labelled_df = classify_sentiment(df)
    labelled_df.to_excel(sentiment_file_path + sentiment_file_name, index = False)

def _5_topics_classifier(
        sentiment_file_path: str = file_path['sentiment_labelled'],
        sentiment_file_name: str = file_name['sentiment_labelled'],
        topics_file_path: str = file_path['topics_labelled'],
        topics_file_name: str = file_name['topics_labelled']
    ) -> None:
    df = pd.read_excel(sentiment_file_path + sentiment_file_name)
    topics_labelled_df = classify_topics(df)
    topics_labelled_df.to_excel(topics_file_path + topics_file_name, index = False)

def _6_get_subject(
        topics_file_path: str = file_path['topics_labelled'],
        topics_file_name: str = file_name['topics_labelled'],
        subject_file_path: str = file_path['get_subject'],
        subject_file_name: str = file_name['get_subject']
    ) -> None:
    enable_proxy()
    NER_preparation()
    df = pd.read_excel(topics_file_path + topics_file_name)
    df['subject'] = df['summarized_en'].apply(get_entity)
    df.to_excel(subject_file_path + subject_file_name, index = False)
    disable_proxy()

def _7_get_cis_with_fuzzy(
        customer_data_file_name:str = file_name['customer_data'],
        subject_file_path: str = file_path['get_subject'],
        subject_file_name: str = file_name['get_subject'],
        final_file_path: str = file_path['final'],
        final_file_name: str = file_name['final'],
    ) -> None:
    df = pd.read_excel(subject_file_path + subject_file_name)
    df_with_cis = fuzzy(customer_data_file_name, df)
    df_with_cis['sub_category'] = None
    df_with_cis = df_with_cis.drop(['translated_content','summarized_en'], axis=1)
    df_with_cis.to_excel(final_file_path + final_file_name, index = False)

def main() -> None:
    # console.log("[bold green][Task] [white]Scraping Gnews")
    logger.info('SCRAPING GNEWS')
    # _1_scraping()

    # time.sleep(0.5)
    # # console.log("[bold green][Task] [white]Translating")
    # logger.info('TRANSLATING')
    # _2_translate()

    time.sleep(0.5)
    # console.log("[bold green][Task] [white]Summarization")
    logger.info('SUMMARIZATION')
    _3_summarize()
     
    # time.sleep(0.5)
    # # console.log("[bold green][Task] [white]Sentiment Labelling")
    # logger.info('SENTIMENT LABELING')
    # _4_sentiment_labeling()

    # time.sleep(0.5)
    # # console.log("[bold green][Task] [white]Classifying Topics")
    # logger.info('CLASSIFYING TOPICS')
    # _5_topics_classifier()

    # time.sleep(0.5)
    # # console.log("[bold green][Task] [white]Extracting Subject")
    # logger.info('EXTRACTING SUBJECT')
    # _6_get_subject()
    
    # time.sleep(0.5)
    # # console.log("[bold green][Task] [white]Fuzzy")
    # logger.info('FUZZY')
    # _7_get_cis_with_fuzzy()
    
    # console.log("[bold green][Task] DONE")
    logger.info('DONE')

if __name__ == '__main__':
    try:
        add_logger(main)
    except Exception as e:
        logger.exception(e)
        raise



