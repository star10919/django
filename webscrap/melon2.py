from bs4 import BeautifulSoup  #오류뜸
import requests

class Melon(object):

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    class_name = []

    def set_url(self):
        self.url = requests.get(f'{self.url}{time}', header=self.headers).text

    def set_class_name(self):
        self.class_name = Melon.url(class_name)

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('-----제목-----')
        ls = soup.find_all("div", {"class": self.class_name[0]})
        for i in ls:
            print(f'{i.find("a").text}')
        print('-----가수-----')
        ls = soup.find_all("div", {"class": self.class_name[1]})
        for i in ls:
            print(f' {i.find("a").text}')

    @staticmethod
    def main():
        m = Melon()
        while 1:
            menu = int(input('0.exit 1.Input 2.Output'))
            if menu == 0:
                break
            elif menu == 1:
                m.set_url(input('스크래핑할 날짜입력 예)2021052513'))
            elif menu == 2:
                m.class_name.append('ellipsis rank01')
                m.class_name.append('ellipsis rank02')
                m.get_ranking()
            else:
                print('wrong number')
                continue

Melon.main()