import time
import os

path = 'C:/Windows/help'
path_normalized = os.path.normpath(path)
print(path_normalized)

count = 0
for dirpath, dirnames, filenames in os.walk(path_normalized):
    # print('*' * 27)
    # print(dirpath, dirnames, filenames)
    # print(os.path.dirname(dirpath))
    # count += len(filenames)
    for file in filenames:
        full_file_path = os.path.join(dirpath, file)
        print(full_file_path)
        secs = os.path.getmtime(full_file_path)
        file_time = time.gmtime(secs)
        print(file_time)
        if file_time[0] == 2013:
            # выводим только файлы за 2013 год
            print(full_file_path, secs, file_time)
# print(count)

# print(__file__, os.path.dirname(__file__))