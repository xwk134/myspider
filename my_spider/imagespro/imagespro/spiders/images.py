import scrapy
from ..items import ImagesproItem
class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['www.duitang.com']
    start_urls = 'https://www.duitang.com/category/?cat=travel#!hot-p{}'

    def start_requests(self):
        #首先腾讯视频的url = 'https://v.qq.com/x/bu/pagesheet/list?append=1&channel=cartoon&iarea=1&listpage=2&offset=0&pagesize=30'
        #我们注意到offset这一项，第一页的offset为0，第二页为30，依次推列
        for i in range(1, 5, 1):

            url = self.start_urls.format(i)
            print(url)
            #这里利用了一个回调机制，即callback, 回调的对象是parse
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = ImagesproItem()
        div_list = response.xpath('//*[@class="mbpho"]')
        for div in div_list:
            item['title'] = div.xpath('./a/img/@alt').get()
            item['scr'] = div.xpath('./a/img/@src').get()
            yield item
