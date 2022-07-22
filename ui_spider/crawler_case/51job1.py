from threading import Thread
from requests_html import HTMLSession
import re
import json
import openpyxl
import mysql.connector
import datetime

infolist = []
def grabOnePage(url):
    session = HTMLSession()
    login_url = 'https://login.51job.com/login.php?loginway=0&isjump=0&lang=c&from_domain=i&url='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
    }
    data = {
        'lang': 'c',
        'action': 'save',
        'from_domain': 'i',
        'with_geetest': 'yes',
        'geetest_challenge': 'a70a4bd96c696147a2245ec352d98061bd',
        'geetest_validate': '98a7978e562058b04d268194c13aca65',
        'geetest_seccode': '98a7978e562058b04d268194c13aca65|jordan',
        'property': '{"frompageUrl":"https:\/\/login.51job.com\/login.php?lang=c","pageUrl":"https:\/\/login.51job.com\/login.php?loginway=0&isjump=0&lang=c&from_domain=i&url="}',
        'distinct_id': '3582d1b61548e08402b1c68b3517fb39',
        'loginname_encrypt': 'vilZ/8/vE4WlsxvgczEupg==',
        'password_encrypt': 'c7UFRMAkHl5GQ82fud7mRQ==',
        'isread': 'on'
    }
    # 使用快代理
    proxies = {
        'http': '202.55.5.209:8090'
    }
    res = session.post(url=login_url, headers=headers, proxies=proxies, data=data)
    print(res.status_code)
    print('获取请求地址：', url)

    # session = HTMLSession()
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    #     'Cookie': 'guid=3582d1b61548e08402b1c68b3517fb39; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; _ujz=MTkwNTQ3Mzg3MA%3D%3D; ps=needv%3D0; 51job=cuid%3D190547387%26%7C%26cusername%3DaxaMNojiBCKchYjIr3EGZfmG2GqJI3QNzUTiZAOd%252FaA%253D%26%7C%26cpassword%3D%26%7C%26cname%3DAP4ghXQDxlf3ofHQBLvOjw%253D%253D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0omRuubM%252Fx9U%26%7C%26cconfirmkey%3D%25241%25242lvSmfSB%2524n0v%252FRcFeAD3KOMnvgdTBu1%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D%25241%2524GHvGfCj0%2524ogh1F50Ftq.j3RWK65EHy0%26%7C%26to%3D6c23269fce09e59e20831b0dd23c93bd6296087d%26%7C%26; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAPython+%BF%AA%B7%A2%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; slife=lastlogindate%3D20220605%26%7C%26; ssxmod_itna2=YqAxB70=Keqmq0Ie0d4kRGG8Ye0QD0iDglBGgD4nI3wxxDsQ8ieDLQM7TDRD4N0FiKoD3eHrKBi8CYe7zjPp7TIx13kocGTdzPyTUFp+ui9E8G1uDukSA4xHHOHXpx9k90r4tLdIGY5TDn+131yGr=pOqKWGzQDQozG=qRG5yQGqtm9GKATw87TrF3bpqemqbR0QaIh=f8gpa33E/0FG2SwAxRBd9eYEcQf=QfxkYdE52gIRxPyT=KvA2t0WwU8CgUftZUS=zH307d/9qf12b4zSqRdgrOtlmLWlURzCF4LSaKp09Ms/7n=8eMePxOWi4ARtp/YA417i7WWYBQmmxwB/Y7jK7Vme/+bjI7iYpxkFMAPgKAov75de3yY3oa4Hu4N5MWRoaaGtow0OCmOpb9tPpO9O4UOp+TrLnr=ueOwfKAN0IxOp/nGlb0IGrG4WQGSt0qtlIzW+O70iAo82xrEqtWMi8LascOMbSzwbPdqAgrkpOSLOaxDKTTMaKx+aORDrE027UMaYdKFtDDLxD2/xYGDLWaKlGDD=; ssxmod_itna=QuiQAIxUODk8P0dD=p7E1IuxDIE4DtPTDRC1x05beGzDAxn40iDtPPNP9Pa9azATYPE4tB4GCl6b7vaYdeSOhWtg140aDbqGkqt=o4GGfxBYDQxAYDGDDPDo2PD1D3qDkD7O1lS9kqi3DbO=Df4DmDGAc3qDgDYQDGMP6D7QDIk6Kl7=ec+rSAWUxijG4FqDMjeGXtictFqRak6qZiCnbw2qDCEq1dAw4l1GoSY0W3qGyiKGujwUZB+b11wXM4jvobEm0U3mYt7Pq4xo+1YQetYmqiRC33Eh14EeGl94zjADxD=='
    # }
    res = session.get(url=url, headers=headers, proxies=proxies, timeout=10)
    res.encoding = 'gb2312'
    #print(res.html.html)
    rule = r'window.__SEARCH_RESULT__ = (.*?)</script>'  # 正则规则
    slotList = re.findall(rule, res.html.html)
    list = json.loads((slotList[0]))
    print(list)
    list1 = list['engine_jds']
    print(list1)
    today = datetime.datetime.today()
    year = today.year
    print(year)
    list2 = []
    for idx in range(len(list1)):
        dict = {
            'position': list1[idx]['job_title'],  # 职位信息
            'company': list1[idx]['company_name'],  # 公司名称
            'pay': list1[idx]['providesalary_text'],  # 薪资
            'treatment': list1[idx]['jobwelf'],     # 福利待遇
            'site': list1[idx]['workarea_text'],        # 公司地址
            'time': str(year)+'-'+list1[idx]['updatedate']        # 发布时间
        }
        list2.append(dict)
    print(list2)

    row = len(list2)
    print(f'{url}-------本页共抓取到{row}条数据')
    for x in range(2, row+2):
        for a, b in list2[x-2].items():
            #print(list2[x-2].items())
            # 保存第一页信息数据
            infolist.append(b)


theadlist = []
for pageIdx in range(1, 21):
    url = f'https://search.51job.com/list/000000,000000,0000,00,9,99,python%2520%25E5%25BC%2580%25E5%258F%2591,2,{pageIdx}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    thread = Thread(target=grabOnePage,
                    args=(url,)
                    )
    thread.start()
    # 把线程对象都存储到 threadlist中
    theadlist.append(thread)

for thread in theadlist:
    thread.join()
print(theadlist)
book = openpyxl.Workbook()
sh = book.active
# 修改当前 sheet 标题为 工资表
sh.title = 'python招聘信息'
# 写入标题
sh['A1'] = '职位信息'
sh['B1'] = '公司名称'
sh['C1'] = '薪资'
sh['D1'] = '福利待遇'
sh['E1'] = '公司地址'
sh['F1'] = '发布时间'
print(infolist)
print(f'总共抓取到{int(len(infolist)/6)}条招聘信息数据')

# 开始写入数据
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin",
  database="test",
  buffered=True
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
try:
    mycursor.execute("CREATE TABLE 51job"
                     " (id INT AUTO_INCREMENT PRIMARY KEY comment '主键',"
                     "position VARCHAR(255) comment '职位信息',"
                     "company VARCHAR(255) comment '公司名称',"
                     "pay VARCHAR(255) comment '薪资',"
                     "treatment VARCHAR(255) comment '福利待遇',"
                     "site VARCHAR(255) comment '公司地址',"
                     "time DATE comment '发布时间') ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8")
finally:
    for a in range(0, int(len(infolist)/6)):
        sql = "INSERT INTO 51job (position, company, pay, treatment, site, time) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (infolist[0+a*6], infolist[1+a*6], infolist[2+a*6], infolist[3+a*6], infolist[4+a*6], infolist[5+a*6])
        mycursor.execute(sql, val)
        mydb.commit()  # 数据表内容有更新，必须使用到该语句
        print(f"第{a+1}条招聘信息数据插入成功")

    print('主线程结束')

