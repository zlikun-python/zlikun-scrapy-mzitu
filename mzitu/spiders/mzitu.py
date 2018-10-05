# -*- coding: utf-8 -*-
import scrapy


class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['http://www.mzitu.com/all/']

    def parse(self, response):

        print(response)

        pass
