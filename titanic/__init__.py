from titanic.views.controller import Controller
from titanic.templates.plot import Plot

if __name__ == '__main__':
    controller = Controller()
    while 1:
        menu = int(input('0-exit\n1-data visualization\n'
                         '2-modeling\n'
                         '3-machine learning\n'
                         '4-machine release'))
        if menu == 0:
            break
        elif menu == 1:
            plot = Plot('train.csv')
            #plot.draw_survived_dead()
            #plot.draw_pclass()
            #plot.draw_sex()
            #plot.draw_embarked()
        elif menu == 2:
            df = controller.modeling('train.csv', 'test.csv')  # 알고리즘 짜고 조립하기
        elif menu == 3:
            df = controller.learning('train.csv', 'test.csv')  # 머신러닝 정확도 보기
        elif menu == 4:
            df = controller.submit('train.csv', 'test.csv')
        else:
            continue