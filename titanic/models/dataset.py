from dataclasses import dataclass


@dataclass  #Dataset클래스의 이름은 dataclass임
class Dataset(object): #type정의 무조건 해줘야 함(표준임) // init 알아서 생성됨(만들지 말자)

    context: str
    fname: str
    train: object  # DF는 object로 하기
    test: object
    id: str
    label: str

    @property
    def context(self) -> str:
        return self._context  #_ 접근제한표시  #게터

    @context.setter
    def context(self, context):
        self._context = context   #세터

    @property
    def fname(self) -> str:
        return self._fname

    @fname.setter
    def fname(self, fname):
        self._fname = fname

    @property
    def train(self) -> object:
        return self._train

    @train.setter
    def train(self, train):
        self._train = train

    @property
    def test(self) -> object:
        return self._test

    @test.setter
    def test(self, test):
        self._test = test

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, label):
        self._label = label


