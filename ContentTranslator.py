import json
from DriverSetting import setting_up_driver
from alive_progress import alive_bar
from selenium.common.exceptions import TimeoutException, JavascriptException
import re
from rich import inspect
import func_timeout
from rich.console import Console
from loguru import logger
global console
console = Console()

class GoogleTranslate():
    def __init__(self, df, vercel_domain, source, target):
        self.driver = setting_up_driver()
        self.vercel_domain = vercel_domain
        self.source = source
        self.target = target
        self.df = df
        self.translated_text_list = self.post_with_timeout(self.df)

    def __translate(self, text):
        config_script = """
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "%s/translate",false);
            xhr.setRequestHeader("Content-Type", "application/json"); 
            var data = JSON.stringify({text:"%s",source:"%s",target:"%s"});
            xhr.send(data);
            return xhr.responseText;""" % (self.vercel_domain, text, self.source, self.target)
        response = self.driver.execute_script(config_script)
        response = json.loads(response)
        return response['response']
    
    def remove_slash(self,text):
        cleaned = re.sub('\\n','',str(text))
        cleaned = re.sub('\\\\','',cleaned)
        return cleaned
    
    def double_quote_handler(self,text):
        cleaned = re.sub('"','\\"',text)
        return cleaned
    
    def post(self, df):
        self.response_list = []
        self.checkpoint = 0
        self.text = ''
        with alive_bar(len(df),dual_line=True,force_tty=True) as main_bar:
            while(1):
                try:
                    for index,row in df.iloc[self.checkpoint:].iterrows():
                        self.text = self.remove_slash(row[0])
                        self.text = self.double_quote_handler(self.text)
                        res = self.__translate(self.text)
                        self.response_list.append(res)
                        main_bar()
                        self.checkpoint+=1
                    if(self.checkpoint == len(df)):
                        break
                except TimeoutException:
                    continue
                except JavascriptException:
                    continue

        self.driver.delete_all_cookies()
        self.driver.quit()
        return self.response_list

    def post_with_timeout(self,df):
        try:
            return func_timeout.func_timeout(timeout=1800, func=self.post, args=[df])
        
        except func_timeout.FunctionTimedOut:
            logger.info("[EXECUTION TIMEOUT] MOVE TO THE NEXT STEP")
            self.driver.delete_all_cookies()
            self.driver.quit()
            return self.response_list
        
        except TimeoutException:
            logger.info("[SELENIUM TIMEOUT] MOVE TO THE NEXT STEP")
            self.driver.delete_all_cookies()
            self.driver.quit()
            return self.response_list

        except Exception as e:
            logger.error(e)
            raise
