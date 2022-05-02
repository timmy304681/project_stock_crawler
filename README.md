# project_stock_crawler
## 專案介紹
本專案以Yahoo奇摩股市為例，開發Python網頁爬蟲取得關注的股票當日行情  
包含：  
* crawler()  
* save2sql()  

crawler()方法(Method)為爬取關注的股票當日行情資料，利用python爬蟲module如：requests和BeautifulSoup，解析奇摩股市html，並提取所需股票資訊  
save2sql()方法(Method)提供存入MySQL資料庫的功能，利用pymysql將crawler()爬取的數據存入mysql
