from CleanData import *
from ContentTranslator import *
from ProxySetup import *
from bs4 import BeautifulSoup
from loguru import logger
from DriverSetting import setting_up_driver
from gnews import GNews
from gnews.utils.constants import BASE_URL
from htmldate import find_date
import time
from tqdm import tqdm

import re
import numpy as np
import pandas as pd
from datetime import datetime

from alive_progress import alive_bar
from rich.console import Console
import logging
import os
import sys
import warnings
warnings.filterwarnings('ignore',category=Warning)

# global console
# console = Console()
class CustomGNews(GNews):
    
    def _get_news(self, query):
        url = BASE_URL + query + self._ceid()
        enable_proxy()
        logger.info('Setting Up Configuration')
        self.driver = setting_up_driver()

        logger.info('Accessing GNews XML')
        self.driver.get(url)     
        xml = BeautifulSoup(self.driver.page_source, 'xml')
        
        self.driver.delete_all_cookies()
        disable_proxy()
        return self.__get_articles_with_timeout(xml)
        
    def __get_articles(self, xml):
        self.id = -1
        self.actual_links = []
        self.article_relation_id = []
        self.contents = []
        self.links = []    
        self.pub_date = []
        self.titles = []

        logger.info('Getting Article Data')
        descriptions = xml.find_all('description')[1:]
        items = xml.find_all('item')
        for description in tqdm(descriptions, desc='Container'):
            self.id += 1
            description_text = description.text
            a_tags = BeautifulSoup(description_text,'html.parser').find_all('a')
            for a in tqdm(a_tags, desc='Content', leave=False):
                link = a['href']
                self.driver.get(link) 
                time.sleep(2) 
                
                self.actual_links.append(str(self.driver.current_url)) # store article actual link
                self.article_relation_id.append(self.id) # store id
                p_tags = BeautifulSoup(self.driver.page_source,'html.parser').find_all('p')
                texts = [str(p_tags[i].text) for i in range(len(p_tags))]
                self.contents.append(' '.join(texts)) # store content
                self.links.append(str(link)) # store article link (news.google)
                self.pub_date.append(find_date(self.driver.page_source,outputformat="%m-%d-%Y")) # store published date
                self.titles.append(str(self.driver.title)) # store title

        self.driver.delete_all_cookies()
        self.driver.quit()

        logger.info('Creating Dataframe')
        df = self.__make_df(self.actual_link, self.article_relation_id, self.content, self.links, self.pub_date, self.titles)        
        
        logger.info('Cleaning Data')
        df = clean(df)
        df.replace('NaN', np.nan, inplace = True)
        df = df.dropna()
        return df
    
    def __get_articles_with_timeout(self,xml):
        try:
            return func_timeout.func_timeout(timeout=3600, func=self.__get_articles,args=[xml])
        
        except func_timeout.FunctionTimedOut:
            logger.error('[EXECUTION TIMEOUT] MOVE TO THE NEXT STEP')
            logger.info('Creating Dataframe')
            self.driver.delete_all_cookies()
            self.driver.quit()
            df = self.__make_df(self.actual_link, self.article_relation_id, self.content, self.links, self.pub_date, self.titles)        
            
            logger.info('Cleaning Data')
            df = clean(df)
            df.replace('NaN', np.nan, inplace = True)
            df = df.dropna()
            return df
        
        except TimeoutException:
            logger.error('[SELENIUM TIMEOUT] MOVE TO THE NEXT STEP')
            logger.info('Creating Dataframe')
            df = self.__make_df(self.actual_link, self.article_relation_id, self.content, self.links, self.pub_date, self.titles)        
            
            logger.info('Cleaning Data')
            df = clean(df)
            df.replace('NaN', np.nan, inplace = True)
            df = df.dropna()
            return df
        
        except KeyboardInterrupt:
            self.driver.delete_all_cookies()
            self.driver.quit()
            logger.error('[KEYBOARD INTERRUPT] MOVE TO THE NEXT STEP')
            logger.info('Creating Dataframe')
            df = self.__make_df(self.actual_link, self.article_relation_id, self.content, self.links, self.pub_date, self.titles)        
            
            logger.info('Cleaning Data')
            df = clean(df)
            df.replace('NaN', np.nan, inplace = True)
            df = df.dropna()
            return df
        
        except Exception as e:
            logger.exception(e)
            raise
    
    def __make_df(self, actual_link, article_relation_id, content, links, pub_date, titles):
        df = pd.DataFrame({'article_id':article_relation_id,
                        'scrape_date':datetime.now().strftime('%m/%d/%Y  %H:%M:%S WIB'),
                        'published_date':pub_date,
                        'link':actual_link,
                        'title':titles,
                        'content':content})
        return df