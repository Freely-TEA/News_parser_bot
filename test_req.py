
from bs4 import BeautifulSoup
import requests 

url = "https://3dnews.ru/news"
#resp = requests.get(url)
soup = BeautifulSoup(url, 'lxml')
print(soup.prettify())
#code = 'document.getElementsByClassName("entry-date")[25].innerText'
