import pandas as pd

class Conversion(object):

    @staticmethod
    def create_tuple() -> ():  # 1부터 9까지 요소를 가진 튜플을 생성하시오 (return)
        return (1, 2, 3, 4, 5, 6, 7, 8, 9)

    @staticmethod
    def tuple_to_list(tp) -> []:  # 1번 튜플을 리스트로 전환하시오 (return)
        return list(tp)

    @staticmethod
    def int_to_float(ls) -> []:  # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
        return [float(i) for i in ls]

    @staticmethod
    def float_to_list(ls) -> []:  # 3번 실수(float) 리스트를, 정수 리스트로 바꾸시오  (return)
        return [int(i) for i in ls]

    @staticmethod
    def list_to_dictionary(ls) -> {}: # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
        return dict(zip([str(i) for i in ls], ls))

    @staticmethod
    def hello_to_tuple(st) -> ():  # 'hello' 를 튜플로 전환하시오
        return tuple(list(st))

    @staticmethod
    def str_tuple_convert_list(tp) -> []:  # 6번 튜플을 리스트로 전환하시오
        return list(tp)

    @staticmethod
    def dict_convert_dataframe(dt) -> object:  # 5번 딕셔너리를 데이터프레임으로 전환하시오
        return pd.DataFrame.from_dict(dt, orient='index')


    @staticmethod
    def main():
        c = Conversion()
        tp = ()
        ls = []
        dt = {}
        df = pd.DataFrame({})

        while 1:
            m = input('0-exit\n'
                      '1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list\n'
                      '8-dict convert dataframe')
            if m == '0':
                break
                # 1부터 9까지 요소를 가진 튜플을 생성하시오 (return)
            elif m == '1':
                tp = c.create_tuple(tp)
                print(tp)
            # 1번 튜플을 리스트로 전환하시오 (return)
            elif m == '2':
                ls = c.tuple_to_list(tp)
                print(f'ls의 타입 : {type(ls)}')
                print(ls)
            # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '3':
                ls = c.int_to_float(ls)
                print(ls)
            # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
            elif m == '4':
                ls = c.float_to_list(ls)
                print(f'ls의 타입 : {type(ls)}')
                print(ls)
            # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == '5':
                dt = c.list_to_dictionary(ls)
                print(f'dt의 타입 : {type(dt)}')
                print(dt)
            # 'hello' 를 튜플로 전환하시오
            elif m == '6':
                tp = c.hello_to_tuple('hello')
                print(f'tp의 타입: {type(tp)}')
                print(tp)
            # 6번 튜플을 리스트로 전환하시오
            elif m == '7':
                ls = c.tuple_to_list(tp)
                print(f'ls의 타입 : {type(ls)}')
                print(ls)
            # 5번 딕셔너리를 데이터프레임으로 전환하시오
            elif m == '8':
                tp = c.create_tuple()
                ls = c.tuple_to_list(tp)
                dt = c.list_to_dictionary(ls)
                print(dt)
                df = c.dict_convert_dataframe(dt)
                print(f'df의 타입: {type(df)}')
                print(df)
            else:
                continue

Conversion.main()