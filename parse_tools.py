import requests 
import json
import time
import os

def get_page_data(page, stream, user_agent):
	headers = {'User-agent' : user_agent}
	ans = requests.get(stream.format(page=page), headers=headers).json()
	documents = ans['documents']

	for url, data in documents.items():
		with open('res_dump/page{pagenum:03d}_{timestamp}.json'.format(pagenum = page, timestamp = int(time.time())), 'w', encoding='utf-8') as f:
			json.dump(documents, f, indent=2)
