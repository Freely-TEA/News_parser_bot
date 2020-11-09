import logging
import configparser

from bs4 import BeautifulSoup
import requests


url = "https://3dnews.ru/news"
resp = requests.get(url)
if resp.status_code == 404:
    print("ERROR 404")
resp = resp.text

soup = BeautifulSoup(resp, 'html.parser')

print("tag")

print("classes (if 'class=' input 0)")

print("id")

tag = "span"
classes = "class_"
id = "entry-date"

# serch all time string
time_string = soup.findAll(tag, class_ = id)

for num, el in enumerate(time_string):
    print(f"{num}. {el}")

time_num = 0

link_search = time_string[time_num]

print(link_search)

print(link_search.get(classes))