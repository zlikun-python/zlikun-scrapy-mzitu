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
    number = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    cover = scrapy.Field()
    create_time = scrapy.Field()
    tags = scrapy.Field()
    pages = scrapy.Field()


class MzituPhotoItem(scrapy.Item):
    """
    照片实体类
    """
    photo_url = scrapy.Field()
    page_url = scrapy.Field()
    photo_number = scrapy.Field()
    album_number = scrapy.Field()
