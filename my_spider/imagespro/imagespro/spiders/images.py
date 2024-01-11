import scrapy
import time
import json
from ..items import ImagesproItem
class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['www.duitang.com']
    start_urls = 'https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments,is_root,source_link,item,buyable,root_id,status,like_count,sender,album,reply_count&filter_id=头像_萌宠&start={}&_=1659607037087'

    def start_requests(self):
        for i in range(24, 1440, 24):
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
            item['scr'] = data_list['data']['object_list'][x]['photo']['path']
            print(item['scr'])
            item['name'] = data_list['data']['object_list'][x]['album']['name']
            or_time = int(data_list['data']['object_list'][x]['oriAddDatetime'])
            # now = int(time.time())
            times = time.localtime(or_time/1000)
            strtime = time.strftime("%Y-%m-%d %H:%M:%S", times)
            print(strtime)
            item['or_time'] = strtime
            millis = int(round(time.time() * 1000))
            print(millis, or_time)
            if (millis-or_time > 60*60*24*30*1*1000):
                print("采集近1个月内数据完成")
                break
            yield item
