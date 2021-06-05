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
    change_ls = []
    change_money_ls = []

    def set_url(self):
        pass

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        all_div = BeautifulSoup(driver.page_source, 'html.parser')
        print('<<<종목명>>>')
        ls = all_div.find_all("td", {"class": self.class_name[0]})
        for i in ls:
            print(i.find("a").text)
            self.name_ls.append(i.find("a").text)
        print('<<<현재가>>>')
        ls = all_div.find_all("td", {"class": self.class_name[1]})
        for i in ls:
            print(i.find("td").text)
            self.price_ls.append(i.find("a").text)
        print('<<<변동>>>')
        ls = all_div.find_all("td", {"class": self.class_name[2]})
        for i in ls:
            print(i.find("img").text)
            self.change_ls.append(i.find("img").text)
        print('<<<변동폭>>>')
        ls = all_div.find_all("td", {"class": self.class_name[3]})
        for i in ls:
            print(i.find("span").text)
            self.change_money_ls.append(i.find("span").text)
        driver.close()

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
                s.class_name.append("no")
                s.class_name.append("number")
                s.class_name.append("number")
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