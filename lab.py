from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://habr.com';
html = urlopen('https://habr.com/ru/search/?q=laravel&target_type=posts&order=relevance')
bs = BeautifulSoup(html, "html.parser")

# nameList = bs.findAll('a', {'class': 'tm-article-snippet__title-link'})
linkList = bs.findAll('a', {'class': 'tm-article-snippet__title-link'})

# for link in linkList:
#     print(link['href'])
    
for link in linkList:
    print(link['href'])
    print(url + link['href'])
    linkHtml = urlopen(url + link['href'])
    bsLink = BeautifulSoup(linkHtml, "html.parser")
    linkContent = bsLink.findAll('h1', {'class': 'tm-article-snippet__title_h1'})
    print(linkContent.get_text())
    break
