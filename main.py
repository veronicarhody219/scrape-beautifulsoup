import smtplib
import email.mime
import datetime
import pandas as pd

urls = []
from bs4 import BeautifulSoup
import requests
for n in range(10):
    if n == 0: 
        url = "https://ngoisao.vnexpress.net/thoi-trang"
        urls.append(url)
    else:
        url = f'https://ngoisao.vnexpress.net/thoi-trang-p{n}'
        urls.append(url)
articles = []
for url in urls:
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.content, 'html5lib')
    # print(soup.prettify())
    arts = soup.find_all('article', attrs={"class": "art_item thumb-full"})
    # print(arts[1])
    for art in arts:
        article={}
        try:    
            src = art.find('img')['src']
            title = art.find("h2").text.strip()
            link = art.find('a')['href']
        except Exception as e:
            src = None
            desc = None
        article['thumb']= src
        article['title'] = title
        article['link'] = link
        
        articles.append(article)
print(articles)
# print(len(urls))
# print(len(articles))
df_articles = pd.DataFrame(articles)
file_name = "img.json"
df_articles.to_json(file_name)
