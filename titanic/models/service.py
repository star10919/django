from titanic.models.dataset import Dataset
import pandas as pd


class Service(object): #dataset을 service로 가져옴

    dataset = Dataset()

    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)