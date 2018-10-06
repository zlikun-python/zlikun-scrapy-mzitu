import datetime

import requests
from scrapy.http import HtmlResponse

url = 'http://www.mzitu.com/32288'
html = requests.get(url).text

response = HtmlResponse(url=url, body=html.encode('utf-8'))

# 专辑信息
title = response.xpath('//h2[@class="main-title"]/text()').extract_first()
category = response.xpath('//div[@class="main-meta"]/span[1]/a/text()').extract_first()
create_time = response.xpath('//div[@class="main-meta"]/span[2]/text()').extract_first().replace('发布于 ', '')

print(title)
print(category)
print(create_time)

# 专辑封面
cover = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
print(cover)

# 相关专题（标签）
tags = response.xpath('//div[@class="main-tags"]/a/text()').extract()
print(tags)

# 专辑照片数
pages = response.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()').extract_first()

# 组装数据
# {
# 'number': '32288', 'title': 'Beautyleg 美腿写真 No.1043 Lynn', 'url': 'http://www.mzitu.com/32288',
# 'category': '台湾妹子', 'cover': 'http://i.meizitu.net/2014/11/02w01.jpg', 'create_time': datetime.datetime(2014, 11, 2, 13, 36),
# 'tags': ['Beautyleg', 'BeautyLeg-Lynn', '性感美女', '美腿'], 'pages': 18
# }
print({
    'number': url.split('/')[-1],
    'title': title,
    'url': url,
    'category': category,
    'cover': cover,
    'create_time': datetime.datetime.strptime(create_time, '%Y-%m-%d %H:%M'),
    'tags': tags,
    'pages': int(pages)
})
