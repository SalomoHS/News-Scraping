import re
import numpy as np
from DomainCleaner import *

def link_domain_filter(df):
    indexes = []
    for index, link in enumerate(df['link']):
        video_matches = re.findall(r'video', link)
        photo_matches = re.findall(r'foto', link)
        if len(video_matches) != 0 or len(photo_matches) != 0:
            indexes.append(index)
    df.drop(index = indexes, inplace = True)
    return df

def change_to_nan(text):
    temp = len(text)
    if temp > 150:
        return text
    else:
        return 'NaN'

def error_message_check(df):
    indexes = []
    for index, content in enumerate(df['content']):
        match_1 = re.findall(r'(Based on your organization\'s access policies\, access to this web site)', content)
        match_2 = re.findall(r'(This website is using a security service to protect itself from online attacks)', content)
        match_3 = re.findall(r'(The origin web server timed out responding to this request)', content)
        if len(match_1) != 0 or len(match_2) != 0 or len(match_3) != 0:
            indexes.append(index)
    df.drop(index = indexes, inplace = True)
    return df

def get_domain(text):
    link = text.strip('https://')
    domain = re.sub(r'(\/-?\w+.*)', ' ', link)
    splitted_domain = domain.split('.')

    len_validation = len(splitted_domain) > 2
    www_validation = splitted_domain[0].strip() == "www"
    gvt_validation = (splitted_domain[-2].strip() == "go" and splitted_domain[-1].strip() == "id")
    cpy_validation = (splitted_domain[-2].strip() == "co" and splitted_domain[-1].strip() == "id")

    if len_validation and len(splitted_domain) != 3 and cpy_validation:
        return splitted_domain[1]
    elif (len_validation and (not www_validation and gvt_validation) or ((not www_validation and cpy_validation))) or not len_validation:
        return splitted_domain[0]
    else:
        return splitted_domain[1]

def numberify_domain(domain):
    switcher = {
        'detik' : 1,
        'cnnindonesia' : 2,
        'bisnis' : 3,
        'bareksa' : 4,
        'beritasatu' : 5,
        'viva' : 6,
        'liputan6' : 7,
        'kontan' : 8,
        'kompas' : 9,
        'tribunnews' : 10,
        'tempo' : 11,
        'idntimes' : 12,
        'bloombergtechnoz' : 13,
        'okezone' : 14,
        'investor' : 15,
        'tvonenews' : 16,
        'disway' : 17,
        'idxchannel' : 18,
        'republika' : 19,
        'cnbcindonesia' : 20,
        'inews' : 21,
        'jpnn' : 22,
        'gridoto' : 23,
        'bbc' : 24,
        'otodriver' : 25
    }
    return switcher.get(domain, 25)

def call_domain_cleaner(domain, text):
    numberified_domain = numberify_domain(domain)
    match numberified_domain:
        case 1:
            return detik_cleaner(text)
        case 2:
            return cnn_cleaner(text)
        case 3:
            return bisnis_cleaner(text)
        case 4:
            return bareksa_cleaner(text)
        case 5:
            return berita_satu_cleaner(text)
        case 6:
            return viva_cleaner(text)
        case 7:
            return liputan6_cleaner(text)
        case 8:
            return kontan_cleaner(text)
        case 9:
            return kompas_cleaner(text)
        case 10:
            return tribun_cleaner(text)
        case 11:
            return tempo_cleaner(text)
        case 12:
            return idn_cleaner(text)
        case 13:
            return bloomberg_cleaner(text)
        case 14:
            return okezone_cleaner(text)
        case 15:
            return investor_cleaner(text)
        case 16:
            return tv_one_cleaner(text)
        case 17:
            return disway_cleaner(text)
        case 18:
            return idx_cleaner(text)
        case 19:
            return republika_cleaner(text)
        case 20:
            return cnbc_cleaner(text)
        case 21:
            return inews_cleaner(text)
        case 22:
            return jpnn_cleaner(text)
        case 23:
            return gridoto_cleaner(text)
        case 24:
            return bbc_cleaner(text)
        case 25:
            return otodriver_cleaner(text)
        case 26:
            return bisnis_cleaner(text)

def domain_cleaner(given_link, given_content):
    domain = get_domain(given_link)
    cleaned_text = call_domain_cleaner(domain, given_content)
    final_text = change_to_nan(cleaned_text)
    return final_text

def clean(df):
    df = link_domain_filter(df)
    df = error_message_check(df)
    df['cleaned'] = df['content'].apply(change_to_nan)
    df['cleaned'] = df.apply(lambda x: domain_cleaner(x.link, x.content), axis = 1)
    df.dropna(inplace = True)
    return df