# -*- coding: utf-8 -*-
#相应模块的导入 
import numpy as np 
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt 
import seaborn as sns 
from IPython.display import display

plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif':['simhei','Arial']})

#导入链家二手房数据
lianjia_df = pd.read_csv('lianjia.csv')
#数据备份
df = lianjia_df.copy()
#display(df.head(5))
#以‘|’进行分割，分割出来的内容按所规定的列名成列
split1=df['message'].str.split('|',expand=True)
split1.columns=['region','layout','area','direction','decoration','elavator']
display(split1)
'''
pandas.concat数据合并：
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
       keys=None, levels=None, names=None, verify_integrity=False)

objs: series，dataframe或者是panel构成的序列lsit 
axis： 需要合并链接的轴，0是行，1是列 
join：连接的方式 inner，或者outer
详细参考：https://blog.csdn.net/mr_hhh/article/details/79488445

注：append默认沿着列进行拼接，例如：result=df1.append(f2)
'''

'''
#将分隔开的字符与原数据表合并
if type(split1)==type(df):
    #print("---------------同类，可以合并。显示此次合并结果-----------------")
    df=pd.concat([df.drop('message',axis=1),split1],axis=1)
#    display(df.head(5))
else:
    print("--------------类型不同，不可合并！----------------")
#将floor栏信息分开
split2=df['floor'].str.split('-',expand=True)
split2.columns=['storey','location']
display(split2)
#将分隔开的字符与原数据表合并
df=pd.concat([df.drop('floor',axis=1),split2],axis=1)
display(df.head(5))
#将popularity栏信息分隔开
split3=df['popularity'].str.split('/',expand=True)
split3.columns=['attention','view_times','release_date']
display(split3)
#将分隔开的字符与原数据表合并
df=pd.concat([df.drop('popularity',axis=1),split3],axis=1)
display(df.head(5))

display(df)
# 重新摆放列位置
columns = ['region', 'location', 'layout', 'storey',  'area', 'elavator', 
           'direction', 'decoration', 'perPrice', 'totalPrice','view_times',
           'attention','release_date']
df = pd.DataFrame(df, columns = columns)
display(df.head(5))
'''

#
##检查缺失值情况
#df.info()
#
#'''
#可以看出总共条数据，其中elavator数据有些微缺失
#'''
#'''计算数据的一些特征值'''
##print(type(df))  #df为DataFrame类
##生成描述性统计数据
#display(df.describe())
##df_mean =df.groupby('region')['perPrice'].mean()
##display(df_mean)
#
##df_count = df.groupby('location')['perPrice'].count()
#
#
#plt.figure(figsize=(10,6))
#plt.rc('font',family='simhei',size=13)
#plt.title(u'各区域平均房价')
#plt.xlabel(u'武汉区域')
#plt.ylabel(u'平均房价')
#plt.bar(df_mean.index,df_mean.values,color='b')
#plt.show()

