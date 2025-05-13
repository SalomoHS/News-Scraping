# yang dipakai dari file ini cuma get_entity ya bos, ntar dipanggilnya tinggal tulis
# from EntityRecognizer import get_entity
import re
import spacy
import pandas as pd
from ProxySetup import *
from LoadConfig import file_path
from loguru import logger
from rich.console import Console
console = Console()

def NER_preparation():
    logger.info("Load Entity Recognition Model")
    global nlp
    nlp = spacy.load(file_path['model_entity_recognizer'])

    # enable_proxy()
    # console.log('[bold cyan][Info] [white]Getting Stock Codes')
    # global stocks
    # stocks = get_stock_code_and_holder()
    # disable_proxy()

    logger.info("Getting Stock Codes")
    global stocks
    stocks = pd.read_excel(file_path['file_stock_list'], index_col = 'Kode').to_dict()['Nama Perusahaan']

    logger.info("Load Abbreviation File")
    global expansion_and_company_name
    expansion_and_company_name = pd.read_excel(file_path['file_abbreviation_for_NER'], index_col = 'Abbrev and Products').to_dict()['Expansion or Company Name']

def extract_entities(text):
    doc = nlp(text)
    entity = []
    for ent in doc.ents:
        tag_list = ["ORG", "PERSON", "LAW"]
        if ent.label_ in tag_list:
            entity.append(ent.text)
    return list(set(entity))

def remove_duplicates(entities):
    seen = set()
    result = []
    for entity in entities:
        if entity not in seen:
            seen.add(entity)
            result.append(entity)
    return result

def remove_subsets(entities):
    multi_word_elements = [item for item in entities if ' ' in item]
    
    substrings = set()
    for multi_word in multi_word_elements:
        substrings.update(multi_word.split())
    
    result = []
    for entity in entities:
        if ' ' in entity:
            result.append(entity)
        elif entity not in substrings:
            result.append(entity)
    return remove_duplicates(result)

def map_stock_code_er(entity):
    if len(entity) == 4:
        if entity == entity.upper():
            if entity in stocks:
                return stocks[entity]
            else:
                return entity
        else:
            return entity
    else:
        return entity

def simple_cleaning(entity):
    cleaned = entity.upper()
    cleaned = re.sub(r"('s)", ' ', cleaned)
    cleaned = cleaned.replace('THE', ' ')
    cleaned = cleaned.replace('PT', ' ')
    cleaned = cleaned.replace('CV', ' ')
    cleaned = cleaned.replace('PERSERO', ' ')
    cleaned = cleaned.replace('TBK', ' ')
    cleaned = re.sub(r'[^\w\s]', ' ', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    cleaned = cleaned.replace('PTE LTD', ' ')
    cleaned = cleaned.replace('PTY LTD', ' ')
    cleaned = cleaned.replace('CO LTD', ' ')
    cleaned = re.sub(r'\s+', ' ', cleaned)
    cleaned = cleaned.strip()
    return cleaned

def final_removal(entities):
    entities = sorted(entities, key = len, reverse = True)
    result = []
    for entity in entities:
        if not any(entity in other for other in result):
            result.append(entity)
    return result

def map_common_abbreviations_and_products(entities):
    expanded = []
    for entity in entities:
        if entity in expansion_and_company_name:
            expanded.append(expansion_and_company_name[entity])
        else:
            expanded.append(entity)
    return expanded

def get_entity(text):
    try:
        raw_entities = extract_entities(str(text))
        low_subset_removed = remove_subsets(raw_entities)
        cleaned_entities = []
        for entity in low_subset_removed:
            stock_code_to_holder = map_stock_code_er(entity)
            cleaned_entities.append(simple_cleaning(str(stock_code_to_holder)))
        return map_common_abbreviations_and_products(final_removal(cleaned_entities))
    
    except Exception as e:
        logger.error(e)
        raise