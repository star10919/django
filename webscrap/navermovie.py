import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver  #네이버꺼 가져오려면

class Navermovie(object):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?'
    class_name = ''  #비워놓으면 input으로 외부에서 값을 받아라 라는 뜻임
    driver_path = 'c:/Program Files/Google/Chrome/chromedriver'
    # driver = 'C://Program Files//Google//Chrome//chromedriver' 이렇게 표기할수도 있다.
    title_ls = []
    dict = {}
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)   #생성자() 처리해주기
        driver.get(self.url)  #크롬드라이버땅에 URL을 주는 것임(내땅에 가져오는게 아님/보안때문에)-그래서프레임워크임
        all_div = BeautifulSoup(driver.page_source, 'html.parser')  #lxml안먹음, 'html.parser'쓰기
        ls = all_div.find_all("div", {"class": "tit3"})
        for i in ls:
            print(i.find("a").text)
            self.title_ls.append(i.find("a").text)
        driver.close()


        # data = soup.find_all("div", {"class": self.class_name})
        # print(soup.find_all("div", {"class": self.class_name}))
        # self.dict = {i:j for i, j in enumerate(data.find("a").text)}
        # for i, j in enumerate(data.a.text):
        #     self.dict[i] = j

    def insert_dict(self):
        # rank = [1, 2, 3, 4, 5, ..., 50]
        rank = []
        for i in range(1, 51):
            rank.append(i)

        for i, j in zip(rank, self.title_ls):
            self.dict[i] = j
            print(f'{i}:{j}')

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/navermovie.csv'
        self.df.to_csv(path, sep=',', na_rep='Nan')

    @staticmethod
    def main():
        nm = Navermovie()
        while 1:
            menu = int(input('0-exit\n1-scrap&Ranking\n2-insert dict\n3-dataframe\n4-csv'))
            if menu == 0:
                break
            elif menu == 1:
                nm.scrap()
            elif menu == 2:
                nm.insert_dict()
            elif menu == 3:
                nm.dict_to_dataframe()
            elif menu == 4:
                nm.df_to_csv()
            else:
                continue

Navermovie.main()