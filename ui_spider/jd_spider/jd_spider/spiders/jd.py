import scrapy
import json
from ..items import JdSpiderItem
import time

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def start_requests(self):
        keywords = ['手机', '笔记本电脑']
        for keyword in keywords:
            for page in range(1, 2):
                url = f'https://search.jd.com/Search?keyword={keyword}&s={page * 56}'
                time.sleep(1)
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response)
        item = JdSpiderItem()
        link = response.xpath(f'//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a/@href').get()
        for x in range(1, 61):
            if link == None:
                print('重新解析')
                item['href'] = 'https:' + response.xpath(f'//*[@id="J_goodsList"]/ul/li[{x}]/div/div[4]/a/@href').get()
                item['xin'] = response.xpath(f'//*[@id="J_goodsList"]/ul/li[{x}]/div/div[8]/i[3]/text()').get()
                # title = response.xpath(f'//*[@id="J_goodsList"]/ul/li[{x}]/div/div[4]/a/@title').get()

            else:
                item['href'] = 'https:' + response.xpath(f'//*[@id="J_goodsList"]/ul/li[{x}]/div/div[3]/a/@href').get()
                item['xin'] = response.xpath(f'//*[@id="J_goodsList"]/ul/li[{x}]/div/div[6]/i[1]/text()').get()
                # title = response.xpath(f'//*[@id="J_goodsList"]/ul/li[{x}]/div/div[3]/a/@title').get()

            yield item
