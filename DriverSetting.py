from fake_useragent import UserAgent
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
import logging
import os
import sys
import warnings

def setting_up_driver():
    ua = UserAgent()
    userAgent = ua.random
    logging.getLogger('selenium').setLevel(level=logging.WARNING)
    options= Options()
    options.add_argument(f'user-agent={userAgent}')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {
        "profile.managed_default_content_settings.images": 2,
        "profile.managed_default_content_settings.stylesheets": 2,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--log-level=3')
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    # options.add_argument("headless=new")
    driver = webdriver.Edge(options=options,service=EdgeService(""))
    return driver

def driver_for_idx():
    ua = UserAgent()
    userAgent = ua.random
    options = Options()
    options.add_argument('headless')
    options.add_argument(f'user-agent={userAgent}')
    options.add_experimental_option("detach", True)
    options.add_argument('log-level=3')
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    # options.add_argument("headless=new")
    driver = webdriver.Edge(options=options,service=EdgeService(""))
    return driver