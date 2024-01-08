# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagesproItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    prodName = scrapy.Field()
    prodCatid = scrapy.Field()
    prodCat = scrapy.Field()
    lowPrice = scrapy.Field()
    highPrice = scrapy.Field()
    avgPrice = scrapy.Field()
    place = scrapy.Field()
    unitInfo = scrapy.Field()
    pubDate = scrapy.Field()

