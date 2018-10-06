# coding:utf-8
# author:zlikun

# xpath selector
# https://docs.scrapy.org/en/latest/topics/selectors.html
# https://www.w3.org/TR/xpath/all/
# https://www.w3.org/TR/2017/REC-xpath-31-20170321/
import requests
from scrapy.http import HtmlResponse
from scrapy.selector import Selector

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Host': 'www.mzitu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Referer': 'http://www.mzitu.com/',
}

# 目前还没太理解scrapy的下载器，这里使用requests来测试xpath选择器
url = 'http://www.mzitu.com/all/'
html = requests.get(url).text

# 链接列表标量及href属性（只取第一条）
# for a_tag in Selector(text=html).xpath('//ul[@class="archives"]//a'):
#     # scrapy.selector.unified.Selector
#     print('text = {}, href = {}'.format(a_tag.xpath('./self::*/text()').extract_first(),
#                                         a_tag.xpath('./self::*/@href').extract_first()))
a_tag = Selector(text=html).xpath('//ul[@class="archives"]//a')[0]
print('text = {}, href = {}'.format(a_tag.xpath('./self::*/text()').extract_first(),
                                    a_tag.xpath('./self::*/@href').extract_first()))

# 等价写法
response = HtmlResponse(url=url, body=html.encode('utf-8'))
a_tag = response.xpath('//ul[@class="archives"]//a')[0]
print('text = {}, href = {}'.format(a_tag.xpath('./self::*/text()').extract_first(),
                                    a_tag.xpath('./self::*/@href').extract_first()))

# 属性、文本同时获取（默认排过序，所以链接在前面，文本在后面）
a_tag_info = response.xpath('//ul[@class="archives"]//a')[0].xpath('./self::*/text() | ./self::*/@href').extract()
# <class 'list'> ['http://www.mzitu.com/152846', '全程高能！美艳尤物卓娅祺撩人心扉的姿势骚气十足']
print(type(a_tag_info), a_tag_info)
