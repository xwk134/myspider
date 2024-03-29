import scrapy
import time
import requests
import json
from ..items import ImagesproItem
class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['www.xinfadi.com.cn']
    start_urls = 'http://www.xinfadi.com.cn/getCat.html'
    urls = 'http://www.xinfadi.com.cn/priceDetail.html'

    def start_requests(self):
        # print("请输入爬取方式:")
        # info = input()
        # if (info == "自动"):
        #
        #     prodCatids = ['1186', '1187', '1189', '1190', '1188', '1203', '1204']
        #     for x in range(0, len(prodCatids)-1):
        #
        #         formdata = {
        #             "prodCatid": prodCatids[x],
        #         }
        #
        #         # 这里利用了一个回调机制，即callback, 回调的对象是parse
        #
        #         yield scrapy.FormRequest(url=self.start_urls, formdata=formdata, callback=self.parse, dont_filter=True)

        # if (info == "关键字"):
        #     print("请输入品名:")
        #     text = input()
        #     print(type(text))
            # headers = {
            #     'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            #     'Accept': '*/*',
            #     'Host': 'www.xinfadi.com.cn',
            #     'Connection': 'keep-alive',
            #     'Content-Type': 'application/json'
            # }
        formdata = {

            'prodName': '大白菜'
        }
        # info = requests.post(url=self.urls, data=formdata)
        # print(info.json())
        # 这里利用了一个回调机制，即callback, 回调的对象是parse
        yield scrapy.FormRequest(url=self.urls, formdata=formdata, callback=self.parse, dont_filter=True)




    def parse(self, response):
        print(response.text)

        data_list = json.loads(response.text)
        print(data_list)
        data_list = response.json()
        info_list = data_list['list']
        item = ImagesproItem()
        print(info_list)
        print(len(info_list))

        #div_list = response.text['objext_list']
        for x in range(0, len(info_list)):
            item['id'] = info_list[x]['id']
            item['prodName'] = info_list[x]['prodName']
            item['prodCatid'] = info_list[x]['prodCatid']
            item['prodCat'] = info_list[x]['prodCat']
            item['lowPrice'] = info_list[x]['lowPrice']
            item['highPrice'] = info_list[x]['highPrice']
            item['avgPrice'] = info_list[x]['avgPrice']
            item['place'] = info_list[x]['place']
            item['unitInfo'] = info_list[x]['unitInfo']
            item['pubDate'] = info_list[x]['pubDate']
            print(item['id'],item['prodName'], item['prodCatid'],item['prodCat'],item['lowPrice'], item['highPrice'],item['avgPrice'],item['place'], item['unitInfo'],item['pubDate'])
            yield item
