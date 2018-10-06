# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MzituAlbumItem(scrapy.Item):
    """
    专辑实体类
    """
    album = scrapy.Field()
    url = scrapy.Field()
