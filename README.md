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

---

### Program Tasks

```mermaid
flowchart TD
    A[Scraping] -->|Scrape business news with Selenium| B[Cleaning]
    B -->|Clean data with regex| C[Summarization]
    C -->|Summarize news with LLM| D[Translate to English]
    D -->|Translate summarized news to English| E[Sentiment Classification]
    E -->|Classify sentiment with fine-tuned BERT| F[Translate to Bahasa Indonesia]
    F -->|Translate back to Bahasa| G[Named Entity Recognition]
    G -->|Extract subject using NER| H[Mapping Customer Id]
    H -->|Map subject to customer id with fuzzy matching| I[Save Result]
    I -->|Save to Excel| J[Note]
    J["(*) Self-host script on Vercel due to internal access restrictions"]
```

1. **Scraping** <br> *Scrape business news topic from google news with python selenium.*
2. **Cleaning** <br> *Clean scraped data with regular expression (regex) from unnecessary pattern, such as advertisement, multiple whitespace, etc.*
3. **\*Summarization** <br> *Summarize news content into 3 sentences using Large Language Model (LLM).*
4. **\*Translate to English** <br> *Translate summarized news to english.*
5. **Sentiment Classification** <br> *Classify sentiment translated news using fine-tuned BERT.*
6. **\*Translate to Bahasa Indonesia** <br> *Translate back news to Bahasa Indonesia.*
7. **Named Entity Recognition** <br> *Extract existing subject from summarized news using Named Entity Recognition (NER).*
8. **Mapping Customer Id** <br> *Map extracted subject with customer id to get customer id using fuzzy matching.*
9. **Save Result** <br> *Save result to excel file.*

*Note* <br>
(*): Script needs to be self-hosted (Vercel) because provider-hosted api (openai and google translate) is not accessible in internal environment. 

---

### Libraries

<p align="left">
<img alt="Selenium" title="Selenium" src="https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=fff"/>
<img alt="Pandas" title="Pandas" src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=fff"/>
<img alt="FastApi" title="FastApi" src="https://img.shields.io/badge/FastAPI-009485.svg?logo=fastapi&logoColor=white"/>
<img alt="HuggingFace" title="HuggingFace" src="https://img.shields.io/badge/Hugging%20Face-FFD21E?logo=huggingface&logoColor=000"/>
</p>

### Cloud Hosting

<p align="left">
<img alt="Vercel" title="Vercel" src="https://img.shields.io/badge/Vercel-%23000000.svg?logo=vercel&logoColor=white"/>
<img alt="Cloudflare" title="Cloudflare" src="https://img.shields.io/badge/Cloudflare-F38020?logo=Cloudflare&logoColor=white"/>
</p>

