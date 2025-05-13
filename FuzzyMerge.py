from ProxySetup import *
from DriverSetting import driver_for_idx

import re
import time
import pandas as pd
from rapidfuzz import fuzz, process
from alive_progress import alive_bar

from loguru import logger
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rich.console import Console
from tqdm import tqdm

tqdm.pandas()
console = Console()

def get_stock_code_and_holder(url = 'https://www.idx.co.id/id/data-pasar/data-saham/daftar-saham'):
    driver = driver_for_idx()
    driver.get(url)
    console.log('[bold cyan][Info] [white]Waiting Element')
    WebDriverWait(driver,450).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select.footer__row-count__select')))
    content_wrapper_select = driver.find_element(By.CSS_SELECTOR, 'select.footer__row-count__select')
    content_wrapper_select.send_keys("All")
    time.sleep(2)
    console.log('[bold cyan][Info] [white]Element Found')
    soup = BeautifulSoup(driver.page_source,'html.parser')
    table = soup.find('table')
    stocks = {}
    with alive_bar(len(table.find_all('tr')[1:]),dual_line=True,force_tty=True) as main_bar:
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            stock_code = cols[0].text.strip()
            company_name = cols[1].text.strip()
            stocks[stock_code] = company_name
            main_bar()

    driver.delete_all_cookies()
    driver.quit()
    return stocks

def data_preparation_fuzzy(entities):
    if not entities:
        return 'UNAVAILABLE'
    else:
        return entities

def clean_symbols(entity):
    entity = re.sub(r'[^\w\s]', ' ', entity)
    entity = entity.strip()
    return entity

def prepare_original_dataframe(df):
    df['subject'] = [i.split(',') for i in df['subject']]
    df = df.explode(['subject'])
    df['subject'] = df['subject'].apply(clean_symbols)
    df['subject'] = df['subject'].apply(data_preparation_fuzzy)
    df = df.reset_index()
    return df
        
def subject_cleaning(text):
    cleaned = text.upper()
    cleaned = re.sub(r'(\(\w+\s?\w+?\))', ' ', cleaned)
    cleaned = cleaned.replace('PT', ' ')
    cleaned = cleaned.replace('COMPANY', ' ')
    cleaned = cleaned.replace('PERSERO', ' ')
    cleaned = cleaned.replace('TBK', ' ')
    cleaned = re.sub(r'[^A-Z0-9]', ' ', cleaned)
    cleaned = cleaned.strip()
    return cleaned

def return_cis(row):
    word_count = (row.subject).split(" ")
    if len(word_count) == 1:
        return ''
    elif (((row.Token_Set_Ratio == 100) and (row.Partial_Ratio > row.Ratio))):
        return row.CIS
    elif row.Token_Sort_Ratio > 65:
        if not row.CIS:
            return ''
        elif ((row.Process_Extract[0][1] >= 86) and (row.Partial_Ratio > 79)) or ((row.Process_Extract[0][1] >= 86) and (row.Partial_Ratio == 100)):  
            return row.CIS
        else:
            return ''
    else:
        return ''
    
def return_cust_name(row):
    word_count = (row.subject).split(" ")
    invalid_score = fuzz.token_sort_ratio(row.subject.upper(), 'TIDAK ADA NAMA PERUSAHAAN YANG TERCANTUM DALAM BERITA TERSEBUT')
    if len(word_count) == 1:
        return row.subject.upper()
    elif (((row.Token_Set_Ratio == 100) and (row.Partial_Ratio > row.Ratio)) and (row.Process_Extract[0][1] >= 86)):
        return row.CUST_NAME
    elif ((invalid_score > 65) or (row.subject.upper() == "NONE")):
        return 'UNAVAILABLE'
    elif (((row.Token_Sort_Ratio > 65) and (row.Process_Extract[0][1] >= 86)) and (row.Partial_Ratio > 79)) or (((row.Token_Sort_Ratio > 65) and (row.Process_Extract[0][1] >= 86)) and (row.Partial_Ratio == 100)):
        return row.Process_Extract[0][0]
    else:
        return row.subject.upper()
    
def fuzzy(customer_log, input_df):
    try:
        customer_log = pd.read_excel(customer_log, dtype={'CIS':object})
        original_df = prepare_original_dataframe(input_df)

        logger.info("Preparing Dataframe for Fuzzy Merge")
        original_df['dummy'] = True
        customer_log['dummy'] = True
        fuzzy_df = pd.merge(original_df, customer_log, on = 'dummy')
        fuzzy_df.drop('dummy', axis=1, inplace=True)

        logger.info("Fuzzy Merging")
        fuzzy_df['Process_Extract'] = fuzzy_df[['subject','CUST_NAME']].apply(lambda x:process.extract(x.subject, [x.CUST_NAME], limit = 1), axis=1)
        fuzzy_df['Ratio'] = fuzzy_df[['subject','CUST_NAME']].apply(lambda x:fuzz.ratio(x.subject, x.CUST_NAME), axis=1)
        fuzzy_df['Partial_Ratio'] = fuzzy_df[['subject','CUST_NAME']].apply(lambda x:fuzz.partial_ratio(x.subject, x.CUST_NAME), axis=1)
        fuzzy_df['Token_Sort_Ratio'] = fuzzy_df[['subject','CUST_NAME']].apply(lambda x:fuzz.token_sort_ratio(x.subject, x.CUST_NAME), axis=1)
        fuzzy_df['Token_Set_Ratio'] = fuzzy_df[['subject','CUST_NAME']].apply(lambda x:fuzz.token_set_ratio(x.subject, x.CUST_NAME), axis=1)
        
        fuzzy_df['Rank_Token_Set_Ratio'] = fuzzy_df.groupby('subject')['Token_Set_Ratio'].rank(ascending = False, method='dense')
        fuzzy_df = fuzzy_df.sort_values(by = ['index', 'subject', 'Token_Sort_Ratio'], ascending = [True, True, False])
        fuzzy_df = fuzzy_df.loc[fuzzy_df.Rank_Token_Set_Ratio == 1]
        fuzzy_df = fuzzy_df.drop_duplicates(subset = 'index', keep = 'first')

        logger.info("Getting CIS & Cust Name")
        fuzzy_df['CIS_new'] = fuzzy_df.progress_apply(return_cis, axis = 1)
        fuzzy_df['SUBJECT_new'] = fuzzy_df.progress_apply(return_cust_name, axis = 1)

        columns = ['index', 'subject', 'CUST_NAME', 'CIS', 'Process_Extract', 'Ratio', 'Partial_Ratio', 'Token_Sort_Ratio', 'Token_Set_Ratio', 'Rank_Token_Set_Ratio']
        fuzzy_df.drop(columns, axis = 1, inplace = True)
        fuzzy_df.rename(columns = {'SUBJECT_new': 'subject', 'CIS_new' : 'cis'}, inplace = True)
        return fuzzy_df
    
    except Exception as e:
        logger.error(e)
        raise