class Configurations():
    def __init__(self):
        self.__file_output = './out/transactions.txt'

    @property
    def file_output(self):
        return self.__file_output
