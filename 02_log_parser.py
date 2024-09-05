# -*- coding: utf-8 -*-
from pprint import pprint


# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах

class Scrolling:
    not_ok = 'NOK'

    def __init__(self, file_name, file_name_out):
        self.file_name = file_name
        self.file_name_out = file_name_out
        self.test = None

    def open(self):
        self.file = open(self.file_name, "r", encoding='utf8')
        self.created = open(self.file_name_out, "w+", encoding='utf8')
        print('Файл {} открыт в режиме чтения, файл {} открыт в режиме записи "+"'.format(self.file_name,
                                                                                          self.file_name_out))

    def processing(self):
        readfile = self.file.readlines()
        for line in readfile:
            ok = 0
            nok = 0
            self.sub_line = str(line[0:17])
            for sek_line in readfile:
                if self.sub_line == str(sek_line[0:17]):
                    if self.not_ok in line:
                        nok += 1
                    else:
                        ok += 1
            if self.testing():
                pass
            else:
                self.created.write(f'{self.sub_line}] + {nok} \n{self.sub_line}] + {ok}\n')
            self.test = self.sub_line
    def testing(self):
        if self.test == self.sub_line:
            return True
        else:
            return False

    def closing(self):
        self.created.close()
        self.file.close()
        print("Оба файла обработаны и закрыты")



file_name = "events.txt"
file_name_out = "out_sec.txt"

book = Scrolling(file_name,file_name_out)
book.open()
book.processing()
book.closing()