import scrapy
import json
from ..items import ImagesproItem
class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['www.duitang.com']
    start_urls = 'https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments,is_root,source_link,item,buyable,root_id,status,like_count,sender,album,reply_count&filter_id=头像_女生&start={}'

    def start_requests(self):
        for i in range(0, 1201, 120):
            url = self.start_urls.format(i)
            #这里利用了一个回调机制，即callback, 回调的对象是parse
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print(response)
        data_list = json.loads(response.text)
        info_list = data_list['data']['object_list']
        item = ImagesproItem()
        print(len(info_list))
        #div_list = response.text['objext_list']
        for x in range(0, len(info_list)):
            item['scr'] = data_list['data']['object_list'][x]['album']['covers'][0]
            item['name'] = data_list['data']['object_list'][x]['album']['name']
            yield item
