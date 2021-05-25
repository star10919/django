from bs4 import BeautifulSoup
from urllib.request import urlopen
class Bugsmusic(object):
    url = ''

    def __str__(self):
        return self.url


# https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01   (차트 창 url)
    @staticmethod
    def main():
        bugs = Bugsmusic()
        while 1:
            menu = int(input('0.Exit\n1.Input URL\n2.Get Ranking\n3.'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('Input Url')
            elif menu == 2:
                print(f'Input URL is {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')

                print('-----------------ARTIST RANKING----------------')
                count = 0
                for i in soup.find_all(name='p', attrs=({"class": "artist"})):
                    count += 1
                    print(f'{str(count)}위')
                    print(f'ARTIST: {i.find("a").text}')

                print('-----------------TITLE RANKING----------------')
                count = 0
                for i in soup.find_all(name='p', attrs=({"class": "title"})):
                    count += 1
                    print(f'{str(count)}위')
                    print(f'TITLE: {i.find("a").text}')
            else:
                print('wrong number')
                continue

Bugsmusic.main()