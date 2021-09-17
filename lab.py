import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://habr.com';
html = urlopen('https://habr.com/ru/search/?q=laravel&target_type=posts&order=relevance')
bs = BeautifulSoup(html, "html.parser")

linkList = bs.findAll('a', {'class': 'tm-article-snippet__title-link'})

file = open('file.csv', 'w')

with file:
    
    writer = csv.writer(file)

    fieldnames = ['link', 'title', 'author', 'rating', 'tags']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    for link in linkList:
        linkHtml = urlopen(url + link['href'])
        bsLink = BeautifulSoup(linkHtml, "html.parser")

        title = bsLink.find('h1', {'class': 'tm-article-snippet__title_h1'}).get_text()
        author = bsLink.find('a', {'class': 'tm-user-info__username'}).get_text().strip()
        rating = bsLink.find('span', {'class': 'tm-votes-meter__value_medium'}).get_text()

        tagList = bsLink.findAll('a', {'class': 'tm-article-body__tags-item-link'})

        tags = []

        for tag in tagList:
            tags.append(tag.get_text().strip())

        writer.writerow({'link': url + link['href'], 'title': title, 'author': author, 'rating': rating, 'tags':tags})

print('CSV done!')
