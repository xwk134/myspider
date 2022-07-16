# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# pip install redis==2.10.6
from redis import Redis
class MovieproPipeline(object):
    conn = None
    def open_spider(self, spider):
        self.conn = Redis(host='192.168.37.131', port=6379)

    def process_item(self, item, spider):
        print('有新的数据正在入库')
        self.conn.lpush('movie_data', item)
        return item
