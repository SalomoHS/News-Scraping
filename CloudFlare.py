from DriverSetting import setting_up_driver
from selenium.common.exceptions import TimeoutException, JavascriptException
from ProxySetup import *
import re
from loguru import logger
from alive_progress import alive_bar
import func_timeout
from nltk.tokenize import sent_tokenize
import re
import time

class Summarizer():
    def __init__(self, vercel_domain, api, user_id, model, df):
        self.driver = setting_up_driver()
        self.vercel_domain = vercel_domain
        self.api = api
        self.user_id = user_id
        self.model = model
        self.df = df
        self.summarized_text_list = self.summarize_with_timeout(self.df)

    def post(self, text):
        config_script = """
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "%s/summarize",false);
            xhr.setRequestHeader("Content-Type", "application/json"); 
            var data = JSON.stringify({"api":"%s","user_id":"%s","model":"%s","text":"%s"});
            xhr.send(data);
            return xhr.responseText;""" % (self.vercel_domain, 
                                           self.api, self.user_id, 
                                           self.model, text)
        response = self.driver.execute_script(config_script)
        return response.strip('"')
    
    def double_quote_handler(self,text):
        cleaned = re.sub('"','\\"',str(text))
        return cleaned
    
    def clean_genai_result(self, text):
        text = str(text)
        temp = re.sub(r'^...','',text)
        temp = re.sub(r'\\n\\n\d\.','',temp)
        temp = re.sub(r'\[','',temp)
        temp = re.sub(r']','',temp)
        temp = re.sub(r"\\n\d\.",'',temp)
        temp = re.sub(r"\\n\*",'',temp)
        return temp

    def truncate_sentences(self,text):
        if len(text) >= 800:
            sentences = sent_tokenize(text)
            truncated_sentences = sentences[-4:-1]
            if len(truncated_sentences) == 0:
                return ' '.join(sentences)
            return ' '.join(truncated_sentences)
        else:
            return text

    def summarize(self, df):
        response_list = []
        checkpoint = 0
        
        with alive_bar(len(df),dual_line=True,force_tty=True) as main_bar:
            while(1):
                try:
                    for index,row in df.iloc[checkpoint:].iterrows():
                        text = self.double_quote_handler(row[0])
                        res = self.post(text)
                        time.sleep(1)
                        res = self.clean_genai_result(res)
                        cut_sentences = self.truncate_sentences(res)
                        response_list.append(cut_sentences)   
                        main_bar()
                        checkpoint+=1
                    if(checkpoint == len(df)):
                        break
                except TimeoutException:
                    continue
                except JavascriptException:
                    continue
        self.driver.delete_all_cookies()
        self.driver.quit()
        return response_list
    
    def summarize_with_timeout(self, df):
        try:
            return func_timeout.func_timeout(timeout=3600, func=self.summarize, args=[df])
        
        except func_timeout.FunctionTimedOut:
            logger.error('[EXECUTION TIMEOUT] MOVE TO THE NEXT STEP')
            self.driver.delete_all_cookies()
            self.driver.quit()
            return self.response_list
        
        except TimeoutException:
            logger.error('[SELENIUM TIMEOUT] MOVE TO THE NEXT STEP')
            self.driver.delete_all_cookies()
            self.driver.quit()
            return self.response_list

        except Exception as e:
            logger.error(e)
            raise