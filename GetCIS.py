from FuzzyMerge import *
from LabelData import *
from ContentTranslator import *
from LoadConfig import file_path
import pandas as pd

def get_cis(df):
    # customer_data = '//kp1eucapp01//MagangCSA//Data//Our Customer//CustomerLog.xlsx'
    # print('tescis')
    # customer_data = '//kp1eucapp01//MagangCSA//Script Python//Web Scraping//Gnews//3.0 - Add Summarizer//CustomerLog.xlsx'
    customer_log = pd.read_excel(file_path['file_customer_data'], dtype = {'CIS' : object})
    original_df = pd.DataFrame({'SUBJECT':df})
    # original_df = prepare_original_dataframe(original_df)
    # original_df['summarized'] = original_df['abs_sum_en'].apply(lambda x: translate(x, 'en'))
    # # print('success translate')
    # original_df['sentiment'] = original_df['summarized'].apply(label)
    # print('success label')
    original_df['SUBJECT'] = original_df['SUBJECT'].apply(lambda x: get_company_name(x).upper())
    original_df['SUBJECT_Cleaned'] = original_df['SUBJECT'].apply(subject_cleaning)
    original_df['SUBJECT'] = original_df['SUBJECT'].apply(lambda x: get_company_name(x).upper())
    df = fuzzy(original_df, customer_log)
    # df.drop(['summarized', 'abs_sum_en'], axis = 1)
    # df.to_excel('',index=False)
    return df