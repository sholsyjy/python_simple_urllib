### 一个小爬虫项目

基础爬虫项目，适合初学者使用。html解析使用`BeautifulSoup`库，代码中涉及到了一点点正则表达式和文件IO。

----------
### 使用说明（建议读懂后再修改）

1.安装库
```
pip install beautifulsoup4
```
没有re的话
```
pip install re
```
可能需要`sudo`

2.运行
```
python main.py
```

3.查看log
第一个`argument`为操作，`page`或者`page inside`。第二个为页码，`page inside`没有页码但有序列号和时间与标题。第三个为`http`状态码。详见[这里](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
