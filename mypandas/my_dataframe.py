import pandas as pd

class MyDataframe(object):

    def __init__(self, columns, index):
        self.columns = columns
        self.index = index

    @staticmethod
    def main():
        df = MyDataframe()