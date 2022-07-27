import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from ..items import MovieproItem

class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['www.4567kp.com']
    start_urls = ['http://www.4567kp.com/frim/index1-1.html']
    rules = (
        Rule(LinkExtractor(allow=r'/frim/index1-\d+\.html'), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        print(response)
        conn = Redis(host='192.168.37.131', port=6379)
        detail_url_list= response.xpath('//h4[@class="title text-overflow"]/a/@href').extract()
        for url in detail_url_list:
            ex = conn.sadd('movies_url', 'http://www.4567kp.com'+url)
            #等于1 的时候 说明数据还没有存储到redis中  等于0 的时候 说明redis中已经存在该数据
            if ex == 1:
                yield scrapy.Request(url='http://www.4567kp.com'+url, callback=self.parse_detail)
            else:
                print("网站中无数据更新，没有可爬取得数据！！！")

    def parse_detail(self,response):
        item = MovieproItem()
        item['name'] = response.xpath('//div[@class="stui-content__detail"]/h1/text()').extract_first()
        item['actor'] = response.xpath('//div[@class="detail col-pd"]/span/text()').extract_first()
        yield item

