# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import pymysql
import time
#管道可以处理提取的数据，如存数据库

import scrapy
class MySpiderPipeline(object):
    def process_item(self, item, spider):
        #print(item)
        return item

class ImagesproPipeline(ImagesPipeline):
    # 对图片地址发起请求
    def get_media_requests(self, item, info):
        #print(item['scr'])
        # 此处的dont_filter即为去重的函数，将其设置为True则表示不要去重复的链接进行去重
        yield scrapy.Request(item['scr'], dont_filter=False)
    # 指定图片的存储路径
    def file_path(self, request, response=None, info=None):
        filePath = request.url.split('/')[-1]+'.png'
        filePath1 = filePath.split('.')[0]+'.png'
        print('下载成功：'+filePath1)
        return filePath1

    # 返回给下一个被执行的管道类
    def item_completed(self, results, item, info):
        return item


class mysqlPipeline(object):
    conn = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='47.100.186.122', port=3306, user='root', password='meixi123', database="gvb_db")

    def process_item(self, item, spider):
        try:
            self.cursor = self.conn.cursor()

            sql = "INSERT IGNORE INTO banner_models (created_at,updated_at,path,name,image_type,tag) VALUES ('%s', '%s', '%s','%s', '%s', '%s')" % (item['or_time'], item['or_time'], item['scr'], item['name'], 3, "萌宠")
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
