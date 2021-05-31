from titanic.models.dataset import Dataset
import pandas as pd

if __name__ == '__main__':
    pass

class Service(object): #dataset을 service로 가져옴

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload  #payloaed는 자기 맘대로(되도록이면 가독성 있게 만들기!)
        return pd.read_csv(this.context + this.fname)

    @staticmethod   #알고리즘 시작
    def create_train(this) -> object:  #object로 리턴되는 건 전부 DataFrame임
        return this.train.drop('Survived', axis=1)  #axis 0은 가로/ 1은 세로

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, feature) -> object:  #필요없는 column은 버려라(분석속도빠르게 하기 위해서)
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)
        return this