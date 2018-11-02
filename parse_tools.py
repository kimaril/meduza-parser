import requests 
import json
import time
import os
from bs4 import BeautifulSoup
from unicodedata2 import normalize

def get_page_data(page, stream, user_agent, site_url="https://meduza.io/{0}"):
    headers = {'User-agent' : user_agent}
    ans = requests.get(stream.format(page=page), headers=headers).json()
    urls = [site_url.format(key) for key in ans['documents'].keys()]
    for url in urls:
        page_responce = requests.get(url, headers=headers, timeout=5)

        if page_responce.status_code == 200:
            page_content = BeautifulSoup(page_responce.content, "html.parser")
            textContent = []
            title = page_content.find_all("h1")[0].text
            for i in range(0, len(page_content.find_all("p"))):
                paragraphs = page_content.find_all("p")[i].text
                textContent.append(normalize('NFKD', paragraphs))

            body = "".join(textContent)

            entry = {"title" : title, "body" : body}
            
            with open('res_dump/page{pagenum:03d}_{timestamp}.json'.format(pagenum = page, timestamp = int(time.time())), 'w', encoding='utf-8') as f: 
                json.dump(entry, f, ensure_ascii=False, indent=2)
                
            #print(entry)
            
            
