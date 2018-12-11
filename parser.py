import json

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
		time = row.find_all(class_='posted-on')
		article_list.append({
			'title': title[0].h2.a.text,
			'content': content[0].p.text,
			'date_posted': time[0].time.text + ' 13:30:05',
			'author': 1,
		})

	feeds = []

	for article in article_list:
		with open('posts.json', mode='w') as feedsjson:
			entry = {
				'title': article['title'],
				'content': article['content'],
				'date_posted': article['date_posted'],
				'author': article['author'],
			}
			feeds.append(entry)
			json.dump(feeds, feedsjson, indent = 4, ensure_ascii = False)

def main():
	parse(get_html('http://murdalov.ru'))

if __name__ == '__main__':
	main()