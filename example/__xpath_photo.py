# -*- coding: utf-8 -*-


import requests
from scrapy.http import HtmlResponse

url = 'http://www.mzitu.com/32288/2'
html = requests.get(url).text

response = HtmlResponse(url=url, body=html.encode('utf-8'))

photo_url = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
page_url = response.url
photo_number, album_number = response.url.split('/')[:2:-1]

# {'photo_url': 'http://i.meizitu.net/2014/11/02w02.jpg', 'page_url': 'http://www.mzitu.com/32288/2', 'photo_number': '2', 'album_number': '32288'}
print({
    'photo_url': photo_url,
    'page_url': page_url,
    'photo_number': photo_number,
    'album_number': album_number
})
