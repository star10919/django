from bs4 import BeautifulSoup
import requests
import pandas as pd

class Bugsmusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    df = None

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('===<<제목>>===')
        ls = soup.find_all("p", {"class": self.class_name[1]})
        for i in ls:
            print(f'{i.find("a").text}')
            self.title_ls.append(i.find("a").text)
        print('===<<가수>>===')
        ls = soup.find_all("p", {"class": self.class_name[0]})
        for i in ls:
            print(f'{i.find("a").text}')
            self.artist_ls.append(i.find("a").text)

    def insert_dict(self):
        for i, j in zip(self.title_ls, self.artist_ls):
            self.dict[i] = j
            print(self.dict)

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/practice.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


    @staticmethod
    def main():
        bugs = Bugsmusic()
        while 1:
            m = int(input('0-exit\n1-input time\n2-output ranking\n3-insert dict\n4-dataframe\n5-csv'))
            if m == 0:
                break
            elif m == 1:
                bugs.set_url(input('시간입력'))  #예) chartdate=20210527&charthour=18
            elif m == 2:
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif m == 3:
                bugs.insert_dict()
            elif m == 4:
                bugs.dict_to_dataframe()
            elif m == 5:
                bugs.df_to_csv()
            else:
                continue

Bugsmusic.main()

