import scrapy


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['http://www.bilibili.com/']

    # 重载start_requests方法
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101Firefox / 59.0',
            'Cookie': '_uuid=4026DD3B-8A3D-C26B-D4D4-DC111A3410C386139infoc; buvid3=A582E6F6-2008-4CC2-8E4A-5E20C55C303F148819infoc; rpdid=|(J|lmmumJk)0JuYJ|mJ|Ykl; LIVE_BUVID=AUTO8216351676213948; video_page_version=v_old_home; buvid4=133467EE-D107-4013-C9BF-C9D1714C03BB65744-022022120-TN7vEsA/sXQiFeRZ6VM3KQ==; nostalgia_conf=-1; CURRENT_BLACKGAP=0; i-wanna-go-back=-1; buvid_fp_plain=undefined; b_ut=5; blackside_state=0; is-2022-channel=1; fingerprint=a87c9f5757dc7a8550c11639121c4fbe; SESSDATA=fdfdc4fd,1675306426,ac7b3*81; bili_jct=2945438aa0fd0446ee67b7a4ee5f522c; DedeUserID=446904919; DedeUserID__ckMd5=70eb00ac8b5d440a; buvid_fp=a87c9f5757dc7a8550c11639121c4fbe; bp_video_offset_446904919=690817246085251100; innersign=0; b_lsid=6822581F_1827201029B; b_timer={"ffp":{"333.1007.fp.risk_A582E6F6":"182720108E9","333.1073.fp.risk_A582E6F6":"1826E1A8604","333.1193.fp.risk_A582E6F6":"18270F8FB47","333.337.fp.risk_A582E6F6":"18270F8F357","333.788.fp.risk_A582E6F6":"18270F904B1","333.937.fp.risk_A582E6F6":"1827102302D","333.42.fp.risk_A582E6F6":"18271112BE0"}}; CURRENT_FNVAL=80; sid=8fx0rmac; PVID=1'
        }

        for x in range(1, 11):
            url = f'https://www.bilibili.com/video/BV1B34y1Y7Rq?p={x}'
            # 再次请求到详情页，并且声明回调函数callback，dont_filter=True 不进行域名过滤
            yield scrapy.Request(url=url, headers=headers, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print(response)


