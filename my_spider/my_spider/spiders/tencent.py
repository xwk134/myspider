import scrapy
import pymysql
from ..items import MySpiderItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['v.qq.com']
    start_urls = 'https://v.qq.com/x/bu/pagesheet/list?append=1&channel=cartoon&iarea=1&listpage=2&offset={}&pagesize=30'
    offset = 0
    conn = pymysql.Connect(host='localhost', port=3306, user='root', password='admin', database="test")
    cursor = conn.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS tencent")
    except Exception as e:
        print(e)

    sql = ("CREATE TABLE tencent"
           " (id INT AUTO_INCREMENT PRIMARY KEY comment '主键',"
           "name VARCHAR(255) comment '视频名称',"
           "description VARCHAR(255) comment '视频简介',"
           "href VARCHAR(255) comment '视频地址') ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8")
    cursor.execute(sql)
    conn.commit()
    print("创建表成功")
    cursor.close()
    conn.close()
    # 重写start_requests方法实现多线程爬取，这里的多线程是基于方法的多线程，
    # 并不是通过创建Thread对象来实现，是在一个方法中，一次性把请求交给调度器
    def start_requests(self):
        #首先腾讯视频的url = 'https://v.qq.com/x/bu/pagesheet/list?append=1&channel=cartoon&iarea=1&listpage=2&offset=0&pagesize=30'
        #我们注意到offset这一项，第一页的offset为0，第二页为30，依次推列
        for i in range(0, 301, 30):
            print(i)
            url = self.start_urls.format(i)
            #这里利用了一个回调机制，即callback, 回调的对象是parse
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = MySpiderItem()
        lists = response.xpath('//div[@class="list_item"]')
        for i in lists:
            items['name'] = i.xpath('./a/@title').get()
            items['description'] = i.xpath('./div/div/@title').get()
            items['href'] = i.xpath('./a/@href').get()
            # 对items封装数据后，调用yield把控制权给管道，管道拿到处理后return返回，又回到该程序
            yield items
