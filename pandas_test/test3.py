import pandas as pd
# 读取excle数据
data_1 = pd.read_excel('./51job.xlsx', sheet_name='python招聘信息')
print(data_1)
print(data_1['职位信息'][0])
# 写入excle数据
data_2 = pd.DataFrame({'职位信息': ['Python爬虫工程师', 'Python开发工程师'], '公司名称': ['广州魅熙网络科技有限公司', '广州魅熙网络科技有限公司'], '公司地址': ['江西省南昌市', '江西省九江市'], '发布时间': ['08-12', '08-13']})
data_2.to_excel('51job.xlsx', sheet_name='python招聘信息', index=False)
# 读取csv数据
my_data = pd.read_csv('./51job.csv', encoding='utf-8')
print(my_data)
# 写入csv数据
data_2 = pd.DataFrame({'职位信息': ['Python爬虫工程师', 'Python开发工程师'], '公司名称': ['魅熙网络科技有限公司', '广州魅熙网络科技有限公司'], '公司地址': ['江西省南昌市', '江西省九江市'], '发布时间': ['08-12', '08-13']})
data_2.to_csv('51job.csv', index=False)

