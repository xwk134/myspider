import scrapy


class IpSpider(scrapy.Spider):
    name = 'ip'
    allowed_domains = []

    def start_requests(self):
        url = 'https://ip.900cha.com/'

        for i in range(1):
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        text = response.xpath('//li[@class="list-item mt-2"]').extract_first()
        print(text)
