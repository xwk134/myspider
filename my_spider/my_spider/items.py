# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
class MySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # item定义你要提取的内容（定义数据结构），比如我提取的内容为视频名称和视频描述、视频地址，
    # 我就创建三个变量。Field方法实际上的做法是创建一个字典，给字典添加一个键，暂时不赋值，等待提取数据后再赋值。
    # 下面item的结构可以表示为：{'name':'','descripition':'','href':''}
    name = scrapy.Field()
    description = scrapy.Field()
    href = scrapy.Field()
