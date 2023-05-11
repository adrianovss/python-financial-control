from configurations.configurations import Configurations
from datetime import date


class Utils():
    def __init__(self):
        self.__configurations = Configurations()

    def read_file(self):
        with open(self.__configurations.file_output, 'r') as file:
            return list(map(lambda l: l.replace('\n', ''), file.readlines()))

    def write_file(self, _type, value, description):
        with open(self.__configurations.file_output, 'a+') as file:
            file.write(
                f'\n{str(date.today())} - {_type} - R$ {value} - {description}')
