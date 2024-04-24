#Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
# адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
# а во второй – все остальные. Посчитать количество полученных строк в каждом
# файле.
import re

count1 = 0
count2 = 0

with open ('ip_address.txt' , 'r') as file1, open('output_file1.txt' , 'w') as file2, open('output_file2.txt', 'w') as file3:
    for i in file1:
        if re.match(r'\d{1,3}\.\d{1,3}', i):
            test = i.strip().split('.')
            if int(test[0])>0 and int(test[1])>0:
                file2.write(i)
                count1 += 1
            else:
                file3.write(i)
                count2 += 1

print(count1)
print(count2)