a = 50
b = 100
c = 40
max = a if a > b else b
max = c if c > max else max
print(max)

a = 50
b = 100
c = 40
max = a if a > b else b
max = c if c < max else max
print(max)

c = int(input('Введи число: '))
print('Результат = ', c + 20 if c >= 0 else c - 5)