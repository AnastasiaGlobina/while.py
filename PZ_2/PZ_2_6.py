# Преобразование числа L в сантиметрах в метры (1м = 100см)
number = int(input("Введите число:  "))
if number < 100 :
    print("Число меньше 100")
else:
    l = number // 100
print(l)
