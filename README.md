# project_stock_crawler
## 專案介紹
本專案以Yahoo奇摩股市為例，開發Python網頁爬蟲取得關注的股票當日行情  
包含：  
* crawler()  
* save2sql()  
* gsheet()  

crawler()方法(Method)為爬取關注的股票當日行情資料，利用python爬蟲module如：requests和BeautifulSoup，解析奇摩股市html，並提取所需股票資訊  
save2sql()方法(Method)提供存入MySQL資料庫的功能，利用pymysql將crawler()爬取的數據存入mysql  
gsheet()方法(Method)則是啟用google sheet api，藉著ServiceAccountCredentials獲取授權，直接將資料寫入雲端google sheet  



## 存入mysql後結果呈現


<img width="1201" alt="pic" src="https://user-images.githubusercontent.com/51151276/166199986-e844a35d-94ec-4d28-9538-eeb98e1b5f84.png">




## 本專案使用的python module
BeautifulSoup  
requests  
lxml  
pymysql  
gspread  
ServiceAccountCredentials  


## Reference
https://www.learncodewithmike.com/2020/08/python-scraper-integrate-with-mysql.html
