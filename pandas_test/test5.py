# coding=utf-8
import pandas as pd
# 读取excle数据
data_1 = pd.read_excel('./51job.xlsx', sheet_name='python招聘信息')
print(data_1['薪资'])


