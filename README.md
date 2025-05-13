<p align="center">
  <h3 align="center">News Scraping</h3>
</p>

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&center=true&vCenter=true&width=435&lines=End-to-end+news+scraping" alt="Typing SVG" /></a>
</p>

<p align="center">
  The need for business news data needed as additional information to analyze the financial condition of customers in the bank sector
</p>

<p align="center">
    <img alt="Python" title="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
</p>

<p align="center">
    <img alt="Selenium" title="Selenium" src="https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=fff"/>
    <img alt="Pandas" title="Pandas" src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=fff"/>
    <img alt="FastApi" title="FastApi" src="https://img.shields.io/badge/FastAPI-009485.svg?logo=fastapi&logoColor=white"/>
    <img alt="HuggingFace" title="HuggingFace" src="https://img.shields.io/badge/Hugging%20Face-FFD21E?logo=huggingface&logoColor=000"/>
</p>

<p align="center">
    <img alt="Vercel" title="Vercel" src="https://img.shields.io/badge/Vercel-%23000000.svg?logo=vercel&logoColor=white"/>
    <img alt="Cloudflare" title="Cloudflare" src="https://img.shields.io/badge/Cloudflare-F38020?logo=Cloudflare&logoColor=white"/>
</p>

---

### Program Tasks

1. **Scraping** -- *Scrape business news topic from google news with python selenium.*
2. **Cleaning** -- *Clean scraped data with regular expression (regex) from unnecessary pattern, such as advertisement, multiple whitespace, etc.*
3. **\*Translate to English** -- *Translate summarized news to english.*
4. **\*Summarization** -- *Summarize news content into 3 sentences using Large Language Model (LLM).*
5. **\*Translate to Bahasa Indonesia** -- *Translate back news to Bahasa Indonesia.*
6. **Sentiment Classification** -- *Classify sentiment translated news using fine-tuned BERT.*
7. **Topic Classification** -- *Classify business sub-topics ("EKONOMI MAKRO", "INOVASI DAN TEKNOLOGI", "ISU DAN KONTROVERSI", "KINERJA KEUANGAN", "PENGHARGAAN DAN PENGAKUAN", "PROMOSI PRODUK", "REKOMENDASI INVESTASI", "LAINNYA").*
8. **Named Entity Recognition** -- *Extract existing subject from summarized news using Named Entity Recognition (NER).*
9. **Mapping Customer Id** -- *Map extracted subject with customer id to get customer id using fuzzy matching.*
10. **Save Result** -- *Save result to excel file.*

*Note* <br>
(*): Script needs to be self-hosted (Vercel) because provider-hosted api (openai and google translate) is not accessible in internal environment. 

---

### Project Files
| File Name              | Description                      |
|:-----------------------|:---------------------------------|
| `requirements.txt`         | Python modules dependencies         |
| `CleanData.py`         | Script to to basic clean raw data         |
| `CloudFlare.py`        | Handles request llm hosted by Cloudflare for summarization |
| `ContentTranslator.py` | Handles request to google translate to Translates content      |
| `DomainCleaner.py`     | Advanced cleaning, act differently for each domain |
| `DriverSetting.py`     | Selenium web driver setup and config      |
| `EntityRecognizer.py`  | Handles Named Entity Recognition process  |
| `FuzzyMerge.py`        | Handles fuzzy matching process |
| `GetCIS.py`            | Mapping Customer ID   |
| `LabelData.py`         | Handles sentiment classification   |
| `LoadConfig.py`        | Loads all configuration         |
| `Logger.py`            | Custom logging utility           |
| `Main.py`              | Entry point of the project       |
| `ProxySetup.py`        | Turn on/off proxy settings for scrapers      |
| `Scraper.py`           | Custom web scraping logic               |
| `TopicsClassifier.py`  | Classifies business sub-topics       |

---

### The Authors
<p>
  <img alt="Salomo Hendrian Sudjono" title="Salomo Hendrian Sudjono" src="https://custom-icon-badges.demolab.com/badge/-Salomo%20Hendrian%20Sudjono-blue?style=for-the-badge&logo=person-fill&logoColor=white"/>
  <img alt="Caroline Angelina Sunarya" title="Caroline Angelina Sunarya" src="https://custom-icon-badges.demolab.com/badge/-Caroline%20Angelina%20Sunarya-blue?style=for-the-badge&logo=person-fill&logoColor=white"/>
</p>

