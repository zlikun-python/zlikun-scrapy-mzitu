# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy import Request

from mzitu.items import MzituAlbumItem, MzituPhotoItem


class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['http://www.mzitu.com/all/']

    def parse(self, response):
        """
        专辑列表页解析

        :param response:
        :return:
        """

        # 解析专辑链接列表
        for tag in response.xpath('//ul[@class="archives"]//a'):
            lst = tag.xpath('./self::*/text() | ./self::*/@href').extract()
            # self.log('parse album = {}, url = {}'.format(lst[1], lst[0]))
            # 返回请求（迭代器）
            yield Request(url=lst[0], callback=self.parse_album)

        # # 仅供调试，只返回一个专辑请求
        # yield Request(url='http://www.mzitu.com/130464', callback=self.parse_album)

    def parse_album(self, response):
        """
        专辑页解析

        :param response:
        :return:
        """
        # 专辑信息
        title = response.xpath('//h2[@class="main-title"]/text()').extract_first()
        category = response.xpath('//div[@class="main-meta"]/span[1]/a/text()').extract_first()
        create_time = response.xpath('//div[@class="main-meta"]/span[2]/text()').extract_first().replace('发布于 ', '')
        # 专辑封面
        cover = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
        # 相关专题（标签）
        tags = response.xpath('//div[@class="main-tags"]/a/text()').extract()
        # 专辑照片数
        pages = int(response.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()').extract_first())
        # 当前网页url
        url = response.url
        album_number = url.split('/')[-1]

        # 专辑数据
        yield MzituAlbumItem({
            'number': album_number,
            'title': title,
            'url': url,
            'category': category,
            'cover': cover,
            'create_time': datetime.datetime.strptime(create_time, '%Y-%m-%d %H:%M').ctime(),
            'tags': tags,
            'pages': pages
        })

        # 照片数据（专辑数据是由第一张照片页提取的，但不能漏掉该页照片）
        yield MzituPhotoItem({
            'photo_url': cover,
            'page_url': url,
            'photo_number': 1,
            'album_number': int(album_number),
            'image_urls': [cover],
        })

        # 照片页请求
        yield from [Request(url='/'.join([response.url, str(i)]), callback=self.parse_photo) for i in
                    range(2, pages + 1)]

    def parse_photo(self, response):
        """
        解析照片页

        :param response:
        :return:
        """

        photo_url = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
        page_url = response.url
        photo_number, album_number = response.url.split('/')[:2:-1]

        yield MzituPhotoItem({
            'photo_url': photo_url,
            'page_url': page_url,
            'photo_number': int(photo_number),
            'album_number': int(album_number),
            'image_urls': [photo_url],
        })
