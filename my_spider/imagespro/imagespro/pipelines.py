# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class MySpiderPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item

class ImagesproPipeline(ImagesPipeline):
    # 对图片地址发起请求
    def get_media_requests(self, item, info):
        #print(item['scr'])
        # 此处的dont_filter即为去重的函数，将其设置为True则表示不要去重复的链接进行去重
        yield scrapy.Request(item['scr'], dont_filter=True)
    # 指定图片的存储路径
    def file_path(self, request, response=None, info=None):
        filePath = request.url.split('/')[-1]+'.png'
        filePath1 = filePath.split('.')[0]+'.png'
        print('下载成功：'+filePath1)
        return filePath1

    # 返回给下一个被执行的管道类
    def item_completed(self, results, item, info):
        return item
