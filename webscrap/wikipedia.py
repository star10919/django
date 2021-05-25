class Wikipedia(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return f'{self.url}'

    @staticmethod
    def main():
        while 1:
            menu = int(input('0.Exit\n1.Input URL\n2.Print URL\n'))
            if menu == 0:
                break
            elif menu == 1:
                wiki = Wikipedia(input('Input URL'))
            elif menu == 2:
                print(f'Input URL is {wiki}')
            else:
                print('wrong number')
                continue

Wikipedia.main()
