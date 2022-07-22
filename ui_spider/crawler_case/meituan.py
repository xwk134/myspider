from threading import Thread
from requests_html import HTMLSession

infolist = []
def grabOnePage(url):
    print('获取请求地址：', url)
    session = HTMLSession()
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
        'Cookie': '__mta=256758324.1656043194324.1656076718037.1656120889790.13; _ga_LYVVHCWVNG=GS1.1.1652153907.1.0.1652153913.0; _lxsdk_cuid=1816c480a44c8-06c2b5efb09ea6-977173c-1fa400-1816c480a44c8; _hc.v=b4cb3b92-6b8c-8ae3-6111-1de7c5fb5262.1655467882; uuid=e8a2150ee1e643e28fe4.1656042804.1.0.0; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; mtcdn=K; _lxsdk=1816c480a44c8-06c2b5efb09ea6-977173c-1fa400-1816c480a44c8; ci=83; rvct=83%2C1; client-id=91588e7d-dd55-4678-b954-7956580164fc; lat=28.68914; lng=115.90915; userTicket=beQKrfpLGewySpBgBXZBsZewqtDELXoNDhwjrznX; _ga=GA1.1.1090014106.1652153908; _ga_95GX0SH5GM=GS1.1.1656121214.1.0.1656121220.0; u=382767655; n=%E5%B2%81%E6%9C%881314%EF%BC%81%EF%BC%81; lt=pCLSMtYLAwVqLoWa-UddHvu_8XEAAAAAjBIAALzfMcohCcFhjviNVHaqSCINQNRtzDIZwcuJzkTnvuyUTVDmdag6T06ovOpi2ZsJRA; mt_c_token=pCLSMtYLAwVqLoWa-UddHvu_8XEAAAAAjBIAALzfMcohCcFhjviNVHaqSCINQNRtzDIZwcuJzkTnvuyUTVDmdag6T06ovOpi2ZsJRA; token=pCLSMtYLAwVqLoWa-UddHvu_8XEAAAAAjBIAALzfMcohCcFhjviNVHaqSCINQNRtzDIZwcuJzkTnvuyUTVDmdag6T06ovOpi2ZsJRA; token2=pCLSMtYLAwVqLoWa-UddHvu_8XEAAAAAjBIAALzfMcohCcFhjviNVHaqSCINQNRtzDIZwcuJzkTnvuyUTVDmdag6T06ovOpi2ZsJRA; unc=%E5%B2%81%E6%9C%881314%EF%BC%81%EF%BC%81; firstTime=1656128480852; __mta=256758324.1656043194324.1656128207542.1656128481139.25; _lxsdk_s=18198cd2c43-f87-ad5-024%7C382767655%7C128'
    }
    proxies = {
        'https': 'http://202.162.37.68:8080'
    }

    res = session.get(url=url, headers=headers, proxies=proxies, timeout=10)
    res.encoding = 'gb2312'
    info = res.html.html
    #print(info)
    titles = res.html.xpath("//a[@class='item-title']/text()")
    links = res.html.xpath("//a[@class='item-title']/@href")
    for x in range(0, len(titles)):
        print('店铺名称：', titles[x], 'https:'+links[x])
        res1 = session.get(url='https:'+links[x], headers=headers, proxies=proxies, timeout=10)
        res1.encoding = 'gb2312'
        titles1 = res1.html.xpath("//div[@class='item']/a/span/text()")
        phone = res1.html.xpath("//div[@class='item']/span[2]/text()")
        time = res1.html.xpath("//*[@id='lego-widget-play-mt-poi-001-000']/div/div[2]/div[1]/div[2]/div[3]/span[2]/text()")
        print('店铺地址：', titles1[0])
        print('联系方式：', phone[0])
        print('营业时间：', time[0])

theadlist = []
for pageIdx in range(2, 3):
    url = f'https://nc.meituan.com/xiuxianyule/pn{pageIdx}/'
    thread = Thread(target=grabOnePage,
                    args=(url,)
                    )
    thread.start()
    # 把线程对象都存储到 threadlist中
    theadlist.append(thread)
for thread in theadlist:
    thread.join()
print('线程数：', len(theadlist))
