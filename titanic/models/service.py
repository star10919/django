from titanic.models.dataset import Dataset  #dataset을 service로 가져옴
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


class Service(object):  #머신러닝(알고리즘)
    # dataset을 service로 가져옴 // #서비스는 기능(알고리즘)으로 이루어져 있음
    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload  #payload는 자기 맘대로(되도록이면 가독성 있게 만들기!)
        return pd.read_csv(this.context + this.fname)   #딕셔너리파일을 데이터프레임으로 전환

    @staticmethod   #알고리즘(머신러닝) 시작
    def create_train(this) -> object:  #object로 리턴되는 건 전부 DataFrame임
        return this.train.drop('Survived', axis=1)  #axis 0은 '가로축'을 지워라/ 1은 '세로축'을 지워라

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:  #필요없는 column은 버려라(분석속도빠르게 하기 위해서)
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object: #파라미터가 없는 리턴은 없음
        this.train = this.train.fillna({'Embarked': 'S'})  #NA값 fillna하는 코딩/*꼭 딕셔너리 형태로 넣어주기
        this.test = this.test.fillna({'Embarked': 'S'})
        print(f'타입체크 {this.train["Embarked"]}')
        # map 함수를 사용하여 S : 1, C : 2, Q : 3
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        # qcut 으로 bins 값 설정 {this.train["FareBand"].head()}
        bins = [-1, 8, 15, 31, np.inf]
        this.train = this.train.drop(['FareBand'], axis=1)
        for these in this.train, this.test:
            these['FareBand'] = pd.cut(these['Fare'], bins=bins, labels=[1, 2, 3, 4])  # {[labels]:[bins]}
        return this


    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]  #train 한번, test한번 돌릴려고(두번쓰기싫어서)
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False) #'Title' 있는거면 그 값 가져오고, 없으면 column에 'Title' 추가  /#extract(일부분만 가져올 때 사용) Name에서 추출
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            dataset['Title'] = dataset['Title'].fillna(0)  # fillna(0) 0은 호칭이 없는 극빈, 노예
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this

    @staticmethod
    def gender_norminal(this) -> object:
        combine = [this.train, this.test]
        gender_mapping = {'male': 0, 'female': 1}
        for i in combine:
            i['Gender'] = i['Sex'].map(gender_mapping)    # 'Gender' 로 feature 이름 바꾸기
        this.train = combine[0]
        this.test = combine[1]
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)  #unknown(미상)처리 해주려고 "-0.5"넣음
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  #구간 잡아주려고   #np.inf : 그 이상을 한번에 뭉탱이로 잡음
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_title_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5,
                             'Adult': 6, 'Senior': 7}
        combine = [train, test]
        for i in combine:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)  # {key = [labels]: value=[bins]}
            i['AgeGroup'] = i['AgeGroup'].map(age_title_mapping)
        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0) #트레인데이터를 10등분/shuffle=True : 반복

    def accuracy_by_svm(self, this):
        score = cross_val_score(SVC(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10,
                                         shuffle=True,
                                         random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)