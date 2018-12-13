import cookielib
import urllib2
import numpy as np
from bs4 import BeautifulSoup

url_begin = "http://search.cs.com.cn/search?page="
url_end = "&channelid=215308&searchword=A%E8%82%A1&keyword=A%E8%82%A1&token=12.1462412070719.47&perpage=10&outlinepage=5&&andsen=&total=&orsen=&exclude=&searchscope=&timescope=&timescopecolumn=&orderby=&timeline==2018.07"
max_num = 13497

res = urllib2.urlopen(url_begin+"1"+url_end)
print res.getcode()
soup = BeautifulSoup(res.read(), "html.parser", from_encoding="utf-8")
test = soup.find("td", class_="searchresult")
# print np.reshape(test.find_all("td"), (10, 3))[0]


for i in range(1, max_num):
  res = urllib2.urlopen(url_begin+str(i)+url_end)
  print "page "+str(i), res.getcode()
  soup = BeautifulSoup(res.read(), "html.parser", from_encoding="unicode")
  result = soup.find("td", class_="searchresult")
  news_list = np.reshape(result.find_all("td"), (10, 3))
  for news in news_list:
    if unicode(news[0]).__contains__("2018.02"):
      print (news[0])
