#Python網頁爬蟲與MySQL資料庫的整合方式

from bs4 import BeautifulSoup
import requests
import lxml
import pymysql

class Stock:
    #建構式
    def __init__(self, *stock_numbers):
        self.stock_numbers = stock_numbers
        print(self.stock_numbers)
 
    #爬取
    def crawler(self):

        result = list()  # 最終結果

        for stock_number in self.stock_numbers:
            response = requests.get("https://tw.stock.yahoo.com/quote/"+stock_number)
            soup = BeautifulSoup(response.text, "lxml")
        
            #利用「公司名稱」的<h1>標籤、「資料時間」的<span>標籤，以及各自的樣式類別(class)，即可進行元素的定位，
            #再透過BeautifulSoup套件的getText()方法就可以取得其中的資料
            stock_name = soup.find('h1', {'class': 'C($c-link-text) Fw(b) Fz(24px) Mend(8px)'}).getText()

            stock_date = soup.find('span', {'class': 'C(#6e7780) Fz(14px) As(c)'}).getText().replace('資料時間：', '')
            market_date = stock_date[0:10]  #日期
            market_time = stock_date[11:16]  #時間
        
            #利用<ul>標籤及它的樣式類別(class)定位,取得「當日行情資料」清單
            ul = soup.find('ul', {'class': 'D(f) Fld(c) Flw(w) H(192px) Mx(-16px)'})
            items = ul.find_all('li', {'class': 'price-detail-item H(32px) Mx(16px) D(f) Jc(sb) Ai(c) Bxz(bb) Px(0px) Py(4px) Bdbs(s) Bdbc($bd-primary-divider) Bdbw(1px)'})
            # 讀取每一個項目(li)下的第2個<span>標籤資料值，並且存放在元組(Tuple)中
            data = tuple(item.find_all('span')[1].getText() for item in items) 

            #整理資料
            result.append((market_date, stock_name, market_time) + data)
        return result

    #將檔案寫進mysql
    #mysql db資料
    def save2sql(self,stocks):
        db_settings = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "******",
            "db": "stock_db",
            "charset": "utf8"}
        try:
            # 使用pymysql的cursor使資料傳入sql
            conn = pymysql.connect(**db_settings)
 
            with conn.cursor() as cursor:
                #column name要與mysql一致
                sql = """INSERT INTO market(
                    market_date,
                    stock_name,
                    market_time,
                    final_price,
                    opening_price,
                    highest_price,
                    lowest_price,
                    average_price,
                    transaction_value,
                    yesterday_price,
                    quote_change,
                    ups_and_downs,
                    total_volume,
                    yesterday_volume,
                    amplitude)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                #將每一支股票資料傳入MySQL中
                for stock in stocks:
                    cursor.execute(sql, stock)
                conn.commit()
 
        except Exception as ex:
            print("Exception:", ex)




stock = Stock("2330","2303","2603","2609")  #建立Stock物件

print(stock.crawler())
stock.save2sql(stock.crawler())