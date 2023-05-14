import matplotlib.pyplot as plt
import numpy as np
import pandas
import pandas as pd
import tushare as ts
# form = pd.read_csv('penguins_lter.csv',header=0)
# form = form.fillna(0)
# x = form['Culmen Length (mm)'].rank(method="average")
# x = pd.DataFrame(x)
# y = pd.merge(x,form)
# print(y.info)
# # print(y)
# print(form)
pro = ts.pro_api()
df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
