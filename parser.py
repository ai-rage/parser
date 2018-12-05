# Parser on Python

import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
	req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	response = urllib.request.urlopen(req)
	return response.read()

def parse(html):
	soup = BeautifulSoup(html)
	main = soup.find('main', class_='site-main')

	article_list = []

	for row in main.find_all('article'):
		title = row.find_all('header')
		content = row.find_all('div')
		article_list.append({
			'title': title[0].h2.a.text,
			'content': [ content.text for content in content[0].find_all('p')]
		})

	for article in article_list:
		print(article)

def main():
	parse(get_html('http://murdalov.ru'))

if __name__ == '__main__':
	main()