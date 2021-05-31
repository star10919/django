from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset: object = Dataset()
    service: object = Service()

    def modeling(self, train, test) -> object:
        service = self.service  #service인스턴스 돼서 ()안쓰는 거임
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this  #예전데이터가 남아있으면 안되고 덮어써야 돼서 return 쓰는 거임

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        print(f'Train 의 type 은 {type(this.train)} 이다.')
        print(f'Train 의 column 은 {this.train.columns} 이다.')
        print(f'Test 의 type 은 {type(this.test)} 이다.')
        print(f'Test 의 column 은 {this.test.columns} 이다.')
        return this