# -*- coding: utf-8 -*-

import os
from operator import itemgetter
from pprint import pprint


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
#
class Counter:

    def __init__(self, file_name, sort=None):
        self.file_name = file_name
        self.stat = {}
        self.sort = sort

    def count(self):
        with open(self.file_name, "r", encoding='utf8') as file:
            for line in file:
                for char in line:
                    # if 1039 < ord(char) < 1104 or ord(char) == 1025 or ord(char) == 1105:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1

    def printed(self):
        self.stat = self.check_dict()

        summ = 0
        print("+---------" * 2 + "+")
        for i in self.stat:
            print("|{char:^8} + {num:^8}|".format(char=i, num=self.stat[i]))
        print("+---------" * 2 + "+")
        for i in self.stat:
            summ += self.stat[i]
        print("|{total:^8} + {summ:^8}|".format(total="Итого", summ=summ))
        print("+---------" * 2 + "+")

    def check_dict(self):
        if self.sort == True:
            sort_dict = dict(sorted(self.stat.items()))
            return sort_dict
        elif self.sort == False:
            sort_dict = dict(sorted(self.stat.items(), reverse=True))
            return sort_dict
        elif self.sort == None:
            return self.stat
        elif self.sort == "Freq":
            sort_dict = dict(sorted(self.stat.items(), key=lambda item: item[1]))
            return sort_dict


book = Counter('Zhnec.txt', sort="Freq")
book.count()
book.printed()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
