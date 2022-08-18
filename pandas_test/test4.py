# coding=utf-8
import pandas as pd
data_5 = pd.DataFrame({'姓名': ['林某某', '许放羊', '王鱼', '王鱼'], '语文': [87, 82, 67, 67], '数学': [73, 85, 90, 90], '英语': ['89', '95', '95','95']})
print(data_5)
data_5['总分'] = data_5['语文'] + data_5['数学'] + data_5['英语'].astype(int)
print(data_5)
# fix_typo = {'王鱼': '王余'}
# data_5 = data_5.replace(fix_typo)
# print(data_5)
print(data_5.duplicated())  # 查看是否重复
print(data_5.drop_duplicates())  # 丢弃重复数据





