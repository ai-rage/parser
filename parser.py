# Parser on Python

import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
	req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	response = urllib.request.urlopen(req)
	return response.read()

def main():
	print(get_html('http://murdalov.ru'))

if __name__ == '__main__':
	main()