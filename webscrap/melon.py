from bs4 import BeautifulSoup
import requests
import pandas as pd

class Melon(object):

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    class_name = []
    df = None
    title_ls = []
    artist_ls = []
    dict = {}

    def set_url(self):
        self.url = requests.get(f'{self.url}{input("시간입력")}', headers=self.headers)

    def set_class_name(self):
        self.class_name = Melon.url(self.class_name)

    def get_ranking(self):
        soup = BeautifulSoup(self.url.content, 'lxml')
        print('----------제목----------')
        ls = soup.find_all("div", {"class": self.class_name[0]})
        for i in ls:
            print(f'{i.find("a").text}')
            self.title_ls.append(i.find("a").text)
        print('----------가수----------')
        ls = soup.find_all("div", {"class": self.class_name[1]})
        for i in ls:
            print(f' {i.find("a").text}')
            self.artist_ls.append(i.find("a").text)

    def insert_dict(self):
        print('=== enter_insert_dict ===')
        for i, j in zip(self.title_ls, self.artist_ls):
            self.dict[i] = j
        print(self.dict)

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/melon.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = int(input('0-exit\n 1-input time\n'
                            '2-output\n'
                            '3-print dict\n'
                            '4-dict to dataframe\n'
                            '5-df to csv'))
            if menu == 1:
                melon.set_url() #스크래핑할 날짜입력 예)2021052513
            elif menu == 2:
                melon.class_name.append('ellipsis rank01')
                melon.class_name.append('ellipsis rank02')
                melon.get_ranking()
            elif menu == 3:
                melon.insert_dict()
            elif menu == 4:
                melon.dict_to_dataframe()
            elif menu == 5:
                melon.df_to_csv()
            else:
                print('wrong number')
                continue

Melon.main()