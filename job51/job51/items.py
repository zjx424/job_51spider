# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    title=scrapy.Field()
    company=scrapy.Field()
    salary=scrapy.Field()
    address=scrapy.Field()
    职位信息=scrapy.Field()
    公司信息=scrapy.Field()
    上班地点=scrapy.Field()
    职能类别=scrapy.Field()