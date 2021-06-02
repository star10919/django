import pandas as pd

from titanic.models.dataset import Dataset
from titanic.models.service import Service
from sklearn.ensemble import RandomForestClassifier


class Controller(object):  # 후크로 이루어져 있음

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service  # service인스턴스 돼서 ()안쓰는 거임
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this  # 예전데이터가 남아있으면 안되고 덮어써야 돼서 return 쓰는 거임

    def learning(self, train, test):
        this = self.modeling(train, test)
        print(f'사이킷런의 SVC 알고리즘 정확도 : {self.service.accuracy_by_svm(this)} %')

    def submit(self, train, test):
        this = self.modeling(train, test)
        clf = RandomForestClassifier()  # clf 는생산자와 사망자의 분류기
        clf.fit(this.train, this.label)  # train=문제, label=답
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)

    def preprocess(self, train, test) -> object:
        this = self.dataset
        service = self.service
        # 초기 모델 생성
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        # norminal, ordinal 로 정형화
        this = service.embarked_nominal(this)
        this = service.title_norminal(this)
        this = service.gender_norminal(this)
        # 불필요한 feature 제거
        this = service.age_ordinal(this)
        this = service.fare_ordinal(this)
        this = service.drop_feature(this, 'Name', 'Sex', 'Cabin', 'Ticket', 'Age', 'Fare')  #이름을 추출한 뒤 지워야 됨.(위쪽에다 쓰면 안됨) **순서(프로세스)중요**

        self.print_this(this)

        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print('<Type Check>')
        print(this)
        print(f'1. Train 의 type\n{type(this.train)} 이다.')
        print(f'2. Train 의 column\n{this.train.columns} 이다.')
        print(f'3. Train 의 상위 5개 행\n{this.train.head()} 이다.')
        print(f'4. Train 의 null 의 갯수\n {this.train.isnull().sum()}개')
        print(f'5. Test 의 type\n{type(this.test)} 이다.')
        print(f'6. Test 의 column\n{this.test.columns} 이다.')
        print(f'7. Test 의 상위 5개 행\n{this.test.head()} 이다.')
        print(f'8. Test 의 null 의 갯수\n {this.test.isnull().sum()}개')
        print('*' * 100)