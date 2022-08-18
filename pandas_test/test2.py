import numpy as np
import pandas as pd
# 创建数组
demo_arr = np.array([['a', 'b', 'c'], ['d', 'e', 'f']])
# 基于数组创建DataFrame对象
df_obj = pd.DataFrame(demo_arr, columns=['No1', 'No3', 'No2'])
print(df_obj)
# 通过列索引的方式获取一列数据
element = df_obj['No2']
element1 = df_obj.No2
print(element1)
# 增加No4一列数据
df_obj['No4'] = ['g', 'h']
print(df_obj)
# 删除No2一列数据
del df_obj['No2']
print(df_obj)

