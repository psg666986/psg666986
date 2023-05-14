import requests

# c = [7,13,18,23]
# c = np.array(c)
# a = 1.04
# b = []
# for i in range(1,5):
#     b.append(a**i)
# b = np.array(b)
# d = sum(c/b)
# e = 1.04**7
# f = d/e/1.1212**5
# print(6000/d)
# print(c/b)
# print(f)
# h = [3, 7, 8, 9, 13]

# h0 = np.var(h)
# h1 = np.var(h,ddof=1)
# print(h0,h1)
def get_url(URL,)
response = requests.get("https://www.bilibili.com/")

response.encoding = 'utf-8'
print(response.status_code)
from bs4 import BeautifulSoup

