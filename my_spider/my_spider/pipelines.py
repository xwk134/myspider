# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
#管道可以处理提取的数据，如存数据库
class MySpiderPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item

class mysqlPipeline(object):
    conn = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='localhost', port=3306, user='root', password='admin', database="test")

    def process_item(self, item, spider):
        try:
            self.cursor = self.conn.cursor()
            sql = "INSERT INTO tencent(name,description,href) VALUES ('%s', '%s', '%s')" % (item['name'], item['description'], item['href'])
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

