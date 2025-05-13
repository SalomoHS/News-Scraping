import json
from datetime import datetime, timedelta
from operator import attrgetter

__attrs = ('year', 'month', 'day')
__start_date = datetime.now() - timedelta(days = 1)
__start_date = attrgetter(*__attrs)(__start_date)
__end_date = datetime.now()
__end_date = attrgetter(*__attrs)(__end_date) 

file_name = {
    'file_raw': f'{datetime.now().strftime("%Y%m%d")}_news_raw.xlsx',
    'file_summarized': f'{datetime.now().strftime("%Y%m%d")}_news_summarized.xlsx',       
    'file_translated': f'{datetime.now().strftime("%Y%m%d")}_news_translated.xlsx',
    'get_subject':f'{datetime.now().strftime("%Y%m%d")}_news_subject.xlsx',
    'final':f'{datetime.now().strftime("%Y%m%d")}_news_final.xlsx',
    'sentiment_labelled':f'{datetime.now().strftime("%Y%m%d")}_news_labelled.xlsx',
    'topics_labelled':f'{datetime.now().strftime("%Y%m%d")}_news_topics_labelled.xlsx',
    'customer_data':''
}

file_path = {
    'file_customer_data' : '',
    'file_raw_data':'',
    'file_translated': '',
    'file_summarized': '\\Gnews\\3. Summarized\\',
    'file_stock_list' : '\\Gnews\\Entity Extraction Resource\\Daftar Saham  - 20241031.xlsx',
    'file_abbreviation_for_NER' : '\\Gnews\\Entity Extraction Resource\\common-abbreviations-and-products.xlsx',
    'get_subject':'\\Gnews\\6. Get Subject\\',
    'final':'\\Gnews\\(Final Manual)\\',
    'sentiment_labelled':'\\Gnews\\4. Sentiment Labelled\\',
    'topics_labelled':'\\Gnews\\5. Topics Labelled\\',
    'file_fact_table' : '\\Gnews\\',
    'file_common_abbreviations_and_products' : ' Scraping\\Gnews\\4.0\\common-abbreviations-and-products.xlsx',
    'model_sentiment_labeling' : ' Model',
    'model_summarizer' : '-L6-v2',
    'model_entity_recognizer' : '\\en_core_web_lg\\en_core_web_lg-3.7.1',
    'model_topics_classifier' : ''
}

vercel = {
    'gemini':'https://gemini-test-salomohs-salomo-hendrians-projects.vercel.app',
    'google_translate':'https://google-translate-salomohs-salomo-hendrians-projects.vercel.app'
}


cloudfare_config = {
    'api':'5pnUivTXlD-6qAdQT0v_sNYRmFMgH7EaGxjVgt2D',
    'user_id':'6a4d9b68ee082caad2a5a9260dbd6c38',
    'model':'@cf/mistral/mistral-7b-instruct-v0.2-lora',
}

scraper_config = {
    'start_date':__start_date,
    'end_date':__end_date,
    'language':"id",
    'country':"ID",
    'topic':"BUSINESS" 
}

translate_config = {
    'source':'id',
    'target':'en',
}