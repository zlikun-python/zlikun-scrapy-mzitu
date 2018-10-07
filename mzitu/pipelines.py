# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class MzituPipeline(object):
    def process_item(self, item, spider):
        return item


# https://docs.scrapy.org/en/latest/topics/item-pipeline.html#write-items-to-a-json-file
class MzituJsonPipeline(object):

    def open_spider(self, spider):
        self.file = open('.data/mzitu.jl', 'a')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item


# https://www.cnblogs.com/Garvey/p/6691753.html
class MzituImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        """
        网站对图片有Referer校验，所以需要添加Referer消息头

        :param item:
        :param info:
        :return:
        """
        if 'image_urls' in item and 'page_url' in item:
            for image_url in item['image_urls']:
                yield Request(url=image_url,
                              meta={'album_number': item['album_number'],
                                    'photo_number': item['photo_number'],
                                    'image_url': image_url},
                              headers={'Host': 'i.meizitu.net', 'Referer': item['page_url']})

    def file_path(self, request, response=None, info=None):
        """
        对图片文件重命名（默认使用SHA-1值命名），格式：/full/$album_number/$photo_number.$photo_prefix

        :param request:
        :param response:
        :param info:
        :return:
        """
        return u'full/{}/{:03d}.{}'.format(request.meta['album_number'],
                                           request.meta['photo_number'],
                                           request.meta['image_url'].split('.')[-1])
