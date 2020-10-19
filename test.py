from bs4 import BeautifulSoup
import requests
import logging
import aiogram
import asyncio
url = "https://www.playground.ru/news"
resp = requests.get(url)
resp = resp.text
soup = BeautifulSoup(resp, 'html.parser')
tag = "time"
source = "datetime"
ide = ""
pr = soup.findAll(tag, source = ide)
for el in pr:
    print(el)