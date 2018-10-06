# -*- coding: utf-8 -*-

import scrapy

from mzitu.items import MzituAlbumItem


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
            # 返回数据（迭代器）
            item = MzituAlbumItem()
            item['album'] = lst[1]
            item['url'] = lst[0]
            yield item
            # 返回请求（迭代器）
            # yield Request(url=lst[0], callback=self.parse_album)

        pass

    def parse_album(self, response):
        """
        专辑页解析

        :param response:
        :return:
        """

        pass
