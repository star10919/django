#종목 외부에서 주입받기(네이버 증권이용하기-셀레니움사용)
#oop로 짜기(class x, 바로 def)
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

class Stock(object):
    url = 'https://m.stock.naver.com/'
    driver_path = 'c:/Program Files/Google/Chrome/chromedriver'
    class_name = []
    name_ls = []
    price_ls = []

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        all_div = BeautifulSoup(driver.page_source, 'html.parser')
        print('<<<종목명>>>')
        ls = all_div.find_all("a", {"class": self.class_name[0]})
        for i in ls:
            print(i.find("a").text)
            self.name_ls.append(i.find("a").text)
        print('<<<현재가>>>')
        ls = all_div.find_all("td", {"class": self.class_name[1]})
        for i in ls:
            print(i.find("td").text)
            self.name_ls.append(i.find("a").text)


        driver.close()



    def set_url(self):

    @staticmethod
    def main():
        s = Stock()

        while 1:
            m = int(input('0-break\n1-get stock\n2-dict\n3-dataframe\n4-csv'))
            if m == 0:
                break
            elif m == 1:
                s.set_url()
            elif m == 2:
                s.class_name.append("title")
                s.class_name.append("number")

                s.scrap()
            elif m == 3:
                pass
            elif m == 4:
                pass
            elif m == 5:
                pass
            else:
                continue

Stock.main()