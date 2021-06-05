from titanic.models.dataset import Dataset
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

class Service(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod    #알고리즘 시작
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this) -> object:
        return

    @staticmethod
    def drop_features(this) -> object:
        return

    @staticmethod
    def embarked_normial(this) -> object:
        return

    @staticmethod
    def fare_ordinal(this) -> object:
        return

    @staticmethod
    def title_norminal(this) -> object:
        return

    @staticmethod
    def gender_norminal(this) -> object:
        return

    @staticmethod
    def age_ordinal(this) -> object:
        return

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def accuracy_by_sum(this):
        score = cross_val_score(SVC(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10,
                                         shuffle=True,
                                         random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)