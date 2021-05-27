from bs4 import BeautifulSoup
import requests
import pandas as pd

class Bugsmusic(object):

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    title_ls = []
    artist_ls = []
    dict = {}
    time = ''
    class_name = []
    df = None

    def set_url(self):
        self.url = requests.get(f'{self.url}{self.time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('-----가수-----')
        ls = soup.find_all("p", {"class": self.class_name[0]})
        for i in ls:
            print(f'{i.find("a").text}')   #그냥 출력만 하는거지 리스트에 담기는게 아님
            self.artist_ls.append(i.find("a").text)  #리스트에 꼭 담기
        print('-----제목-----')
        ls = soup.find_all("p", {"class": self.class_name[1]})
        for i in ls:
            print(f'{i.find("a").text}')   #그냥 출력만 하는거지 리스트에 담기는게 아님
            self.title_ls.append(i.find("a").text)    #리스트에 꼭 담기

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
        path = './data/bugs.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

    @staticmethod
    def main():
        bugs = Bugsmusic()
        while 1:
            menu = input('0-exit\n 1-input time\n'
                         '2-output\n'
                         '3-print dict\n'
                         '4-dict to dataframe\n'
                         '5-df to csv')
            if menu == 0:
                break
            elif menu == '1':
                bugs.time = input('시간입력')#chartdate=20210527&charthour=16
                bugs.set_url()
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.insert_dict()
            elif menu == '4':
                bugs.dict_to_dataframe()
            elif menu == '5':
                bugs.df_to_csv()
            else:
                print('wrong number')
                continue

Bugsmusic.main()