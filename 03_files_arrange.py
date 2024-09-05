# -*- coding: utf-8 -*-

import os, time, shutil
import zipfile
from pprint import pprint
from zipfile import ZipFile

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
route = 'C:\\Users\\NevO\\PycharmProjects\\Text_scroll\\icons.zip'


class Sorted:
    store = {}

    def __init__(self, route_to_file, route_to_end):
        self.normolized_route = os.path.normpath(route_to_file)
        self.route_to_end = os.path.normpath(route_to_end)
        self.z = None
        self.filename = None
        self.file_extension = None

    def check_zip(self, path):

        self.filename, self.file_extension = os.path.splitext(path)
        if self.file_extension == '.zip':
            return True
        else:
            return False

    def check_file_or_dir(self, path):
        if os.path.isfile(path):
            return True
        else:
            return False

    def open(self):
        if self.check_file_or_dir(self.normolized_route):
            if self.check_zip(self.normolized_route):
                self.z = zipfile.ZipFile(self.normolized_route, 'r')
                print('Файл {} открыт в режиме - чтение'.format(self.filename))
                self.z_processing()
            else:
                print('Укажите путь к папке или "Zip" файлу')
        else:
            print('Обработка применяется к папке {}'.format(self.filename))
            self.processing()

    def processing(self):
        for dirpath, dirnames, filenames in os.walk(self.normolized_route):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                new_route = os.path.join(self.route_to_end, str(file_time[0]), str(file_time[1]))
                os.makedirs(new_route, mode=0o777)
                shutil.copy2(src=str(full_file_path), dst=str(new_route))
        print('Обработка файлов завершена')

    def z_processing(self):
        file_list = self.z.infolist()
        for item in file_list:
            self.store[item.filename] = item.date_time
        for file_name, date in self.store.items():
            new_route = os.path.join(self.route_to_end, str(date[0]), str(date[1]))
            self.z.extract(file_name, new_route)
            self.close()
            print('Обработка файлов завершена')

    def close(self):
        self.z.close()

# # Усложненное задание (делать по желанию)
# # Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# # Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# # Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
