# -*- coding: utf-8 -*-


from scrapy.http import HtmlResponse

url = 'http://www.mzitu.com/32288'
response = HtmlResponse(url=url)

# url
assert response.url == url
assert response.urljoin(url='2') == 'http://www.mzitu.com/2'
assert response.url + '/2' == 'http://www.mzitu.com/32288/2'

response = HtmlResponse(url=url + '/2')
photo_number, album_number = response.url.split('/')[:2:-1]
assert photo_number == '2'
assert album_number == '32288'
