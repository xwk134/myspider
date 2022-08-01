# 给pandas起个别名pd
import pandas as pd
# 创建Series类对象
ser_obj = pd.Series([1, 2, 3, 4, 5])
ser_obj.index = ['a', 'b', 'c', 'd', 'e']
print(ser_obj)

# 传入一个字典创建Series类对象
# year_data = {2001: 17.4, 2002: 20.2, 2003: 23.3}
# ser_obj2 = pd.Series(year_data)
# print(ser_obj2)

# 获取ser_obj的索引
print(ser_obj.index)
# 获取ser_obj的数据
print(ser_obj.values)
print(ser_obj[2])

