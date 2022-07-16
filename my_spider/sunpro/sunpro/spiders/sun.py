import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=']
    # 链接提取器：根据指定规则(正则)进行指定链接的提取
    link = LinkExtractor(allow=r'id=1&page=\d+')

    rules = (
        # 规则解析器：将链接提取器提取到的链接进行规则的解析操作
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        print(response)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
