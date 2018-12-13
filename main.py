import cookielib
import urllib2
import numpy as np
from bs4 import BeautifulSoup, Tag
import re
import os
import httplib

'''
this is an unkown bug with HTTP/1.0 and HTTP/1.1
'''
httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = "HTTP/1.0"

url_begin = "http://search.cs.com.cn/search?page="
url_end = "&channelid=215308&searchword=A%E8%82%A1&keyword=A%E8%82%A1&token=12.1462412070719.47&perpage=10&outlinepage=5&&andsen=&total=&orsen=&exclude=&searchscope=&timescope=&timescopecolumn=&orderby=&timeline==2018.07"
max_num = 13726
path = "./news/"

if not os.path.exists(path):
  os.mkdir(path)

def isWanted(news):
  return news.__contains__("2018.02") or news.__contains__("2018.03") or news.__contains__("2018.04") or news.__contains__("2018.05") or news.__contains__("2018.06")

for i in range(12711, max_num):
  res = urllib2.urlopen(url_begin+str(i)+url_end)
  print "page "+str(i), res.getcode()
  soup = BeautifulSoup(res.read(), "html.parser", from_encoding="unicode")
  result = soup.find("td", class_="searchresult")
  news_list = np.reshape(result.find_all("td"), (10, 3))
  for (index, news) in enumerate(news_list):
    if isWanted(unicode(news[0])):
      page_url = news[0].find("a")["href"]
      page_title_a = news[0].find("a").contents
      page_title = ""
      for html in page_title_a:
        if type(html) is Tag:
          page_title += unicode(html.contents[0])
        else:
          page_title += unicode(html)
      date = news[0].find(string=re.compile("2018[.]0[0-9][.][0-9]{2}")).split(" ")[0].split("\n")[-1]
      time = news[0].find(string=re.compile("2018[.]0[0-9][.][0-9]{2}")).split(" ")[-1].split("\n")[0]
      page_res = urllib2.urlopen(page_url)
      print "page inside", index, page_res.getcode(), date, time, page_title
      page_soup = BeautifulSoup(page_res.read(), "html.parser", from_encoding="unicode")
      contents_div = page_soup.find("div", class_="article-t")
      if type(contents_div) is type(None):
        continue
      contents = contents_div.find_all("p")
      try:
        filename = path + date + '_' + time + '_' + page_title + '.txt'
        fo = open(filename, 'w')
        fo.write(unicode(page_url).encode("utf-8") + "\n")
        for content in contents:
          fo.write(unicode(content.contents[0]).encode("utf-8") + "\n")
        fo.close()
      except IOError, Argument:
        print Argument
        fo.close()


