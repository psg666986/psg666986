import random
import math
import tushare as ts
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dateutil
from matplotlib import pyplot as pkl
datetime1 = dateutil.parser.parse('2001-01-28')
datetime2 = dateutil.parser.parse('2002-JAN-28')
'''上式等于import datetime
datetime2 = datetime.strptime('2001-01-28', '%Y-%m-&d')'''
# b = ord('a')
# print(b)
# a = pd.Series(np.arange(10))
# list1 = []
# for i in range(97,107):
#     list1.append(chr(i))
# print(list1)
# a.index = list1
# print(a)
n = pd.DataFrame({'one':[5,2,3],'two':[9,7,6]},dtype='float')
# print(n)
c = n.mean(axis=1)
sort1 = n.sort_values(by='one')
sort2 = n.sort_values(by='two')
sort3 = n.sort_values(by='two',ascending=False)
'''注意以上区别'''
pd.to_datetime(['2002-02-23','2002-FEB-02'])
pd.date_range('2002-5-21',freq='Y',periods=10)
'''use "pd.date_range?" to consult for the usage '''
pd.date_range('2002-5-21',freq='W',periods=10)#week
pd.date_range('2002-5-21',freq='W-MON',periods=10)#every Monday
pd.date_range('2002-5-21',freq='B',periods=10)#busies day
pd.date_range('2002-5-21',freq='SM',periods=10)#semi-mon
pd.date_range('2002-5-21',freq='T',periods=10)#mintes
'''在console里，如果给变量例如x赋上面的语句的结果值，用x = _'''
x = pd.Series(np.arange(100),index=pd.date_range('2002-5-21',periods=100))
x.resample('W').sum()
x.truncate(after='2002-06-01',before='2002-05-01')
# plt.plot([3,4,5,6],[2,5,6,8])
# plt.show()
ts.set_token('983116f433115bab8d68f595d9ec2e99a339df9f72ef0389c6dc717d')

