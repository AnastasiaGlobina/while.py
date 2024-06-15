"""перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
вложенных подкаталогов выводить не нужно.
 перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
файлов в папке test.
 перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
консоль. Использовать функцию basename () (os.path.basename()).
 перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
привязанной к нему программе. Использовать функцию os.startfile().
 удалить файл test.txt."""


import os


"Задание 1"
path = 'C:/Users/Rostov/PycharmProjects/Старчиков/PZ 11'
files = os.listdir(path)
for file in files:
    if os.path.isfile(os.path.join(path, file)):
        print(file)


"Задание 2"
# os.chdir('C:/Users/Rostov/PycharmProjects/Старчиков')
# os.mkdir('./PZ 17/test/')
# os.mkdir('./PZ 17/test/test1')
# os.rename('./PZ 6/PZ_6-17.py', './PZ 17/test/PZ_6.txt')
# os.rename('./PZ 6/PZ_6(1)-17.py', './PZ 17/test/PZ_6(1).txt')
# os.rename('./PZ 7/PZ_7-17.py', './PZ 17/test/test1/test.txt')

total_size = 0
for dirpath, dirnames, filenames in os.walk('test'):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        file_size = os.path.getsize(filepath)
        total_size += file_size
        print(f"Размер файла {filename}: {file_size} байт")
print(f"Общий размер файлов {total_size} байт")


"Задание 3"
os.chdir('C:/Users/Rostov/PycharmProjects/Старчиков')
short_file = min(os.listdir('PZ 11'), key=len)
print("Файл с самым коротким именем: ", os.path.basename(short_file))


"Задание 4"
# os.chdir('C:/Users/Rostov/PycharmProjects/Старчиков/reports')
# for file in os.listdir():
#     if file.endswith('.pdf'):
#         os.startfile(file)
#         break


"Задание 5"
# os.chdir('C:/Users/Rostov/PycharmProjects/Старчиков/PZ 17')
# os.remove('./test/test1/test.txt')

