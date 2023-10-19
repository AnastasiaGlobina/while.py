n = input ("Введите целое число: ")
while type(n) != int:
    try:
        n  = int (n)
    except ValueError:
        prin("Неправильно ввели! ")
        n = input("Введите целое число: ")



if not (math.fmod(n, 2)):
         print("Четное")
else:
        print("Нечетное")

