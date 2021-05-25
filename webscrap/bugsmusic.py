from bs4 import BeautifulSoup
import requests

class Bugsmusic(object):

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://music.bugs.co.kr/chart'
    class_name = []

    def set_url(self):
        self.set_url = requests.get(f'{Bugsmusic.url}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('-----제목-----')
        ls = soup.find_all("p", {"class": self.class_name['title']})
        for i in ls:
            print(f'{i.find("a").text}')
        print('-----가수-----')
        ls = soup.find_all("p", {"class": self.class_name['artist']})
        for i in ls:
            print(f'{i.find("a").text}')

    @staticmethod
    def main():
        bm = Bugsmusic()
        while 1:
            menu = int(input('0.exit 1.require 2.response'))
            if menu == 0:
                break
            elif menu == 1:
                bm.set_url()
            elif menu == 2:
                bm.get_ranking()
            else:
                print('wrong number')
                continue

Bugsmusic.main()