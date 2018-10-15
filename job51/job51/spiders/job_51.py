# -*- coding: utf-8 -*-
import scrapy
from job51.temp import keylist
from job51.items import Job51Item
import re

key=input('请输入爬取的关键词：')

class Job51Spider(scrapy.Spider):

    name=key
    base_url ='https://search.51job.com/list/030800%252C040000%252C030200,000000,0000,00,9,99,{key},2,{page}.html?lang=c&stype=1'
    start_url=base_url.format(key=key,page=1)
    def start_requests(self):
        yield scrapy.Request(url=self.start_url,callback=self.parse)

    def parse(self, response):
        item=Job51Item()
        datas=response.xpath('//div[@class="el"]/p')
        for data in datas:
            item['url']=data.xpath('.//a/@href').extract_first()
            yield scrapy.Request(url=item['url'],meta={'item':item},callback=self.get_info)
        text=response.xpath('//div[@class="p_in"]//span[@class="td"]/text()').extract_first()
        maxnum=int(re.findall('(\d+)',text)[0])
        for i in range(2,maxnum+1):
            next_url=self.base_url.format(key=key,page=i)
            yield scrapy.Request(url=next_url,callback=self.parse)

    def get_info(self,response):
        item = response.meta['item']
        item['title']=response.xpath('//h1/@title').extract_first() if len(response.xpath('//h1/@title')) > 0 else None
        item['company']=response.xpath('//p[@class="cname"]/a/@title').extract_first() if len(response.xpath('//p[@class="cname"]/a/@title')) > 0 else None
        item['salary']=response.xpath('//div[@class="cn"]/strong/text()').extract_first() if len(response.xpath('//div[@class="cn"]/strong/text()')) > 0 else None
        item['address'] = response.xpath('//p[@class="msg ltype"]/@title').extract_first().replace('\xa0\xa0', '').split('|')[0] if len(response.xpath('//p[@class="msg ltype"]/@title')) > 0 else None
        item['职位信息'] = response.xpath('//div[@class="bmsg job_msg inbox"]/p/text()').extract() if len(response.xpath('//div[@class="bmsg job_msg inbox"]/p/text()')) > 0 else None
        item['公司信息'] = response.xpath('//div[@class="tmsg inbox"]/text()').extract_first() if len(response.xpath('//div[@class="tmsg inbox"]/text()')) > 0 else None
        item['上班地点'] = response.xpath('//div[@class="bmsg inbox"]/p/text()').extract()[1] if len(response.xpath('//div[@class="bmsg inbox"]/p/text()')) > 0 else None
        item['职能类别'] = response.xpath('//div[@class="mt10"]/p/span[@class="el"]/text()').extract_first() if len(response.xpath('//div[@class="mt10"]/p/span[@class="el"]/text()')) > 0 else None
        yield item