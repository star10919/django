from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):  #후크로 이루어져 있음

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service  #service인스턴스 돼서 ()안쓰는 거임
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this  #예전데이터가 남아있으면 안되고 덮어써야 돼서 return 쓰는 거임

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        #초기 모델 생성
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        # 불필요한 feature (Cabin, Ticket) 제거
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        # norminal, ordinal 로 정형화
        this = service.embarked_nominal(this)
        this = service.title_norminal(this)
        # 불필요한 feature (Name) 제거
        this = service.drop_feature(this, 'Name')  #이름을 추출한 뒤 지워야 됨.(위쪽에다 쓰면 안됨) **순서(프로세스)중요**
        this = service.gender_norminal(this)
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print('<Type Check>')
        print(f'Train 의 type 은 {type(this.train)} 이다.')
        print(f'Train 의 column 은 {this.train.columns} 이다.')
        print(f'Train 의 상위 5개 행은 {this.train.head()} 이다.')
        print(f'Train 의 하위 5개 행은 {this.train.tail()} 이다.')
        print(f'Test 의 type 은 {type(this.test)} 이다.')
        print(f'Test 의 column 은 {this.test.columns} 이다.')
        print(f'Test 의 상위 5개 행은 {this.test.head()} 이다.')
        print(f'Test 의 하위 5개 행은 {this.test.tail()} 이다.')
        print('*' * 100)