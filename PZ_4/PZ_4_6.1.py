#Код преабразовывает введенные пользователем числа в их сумму от А до Б включительно
number = int(input ("введите первое число: "))
numbers = int(input ("введите второе число: "))
sum = 0
if number < numbers:
    for i in range(number, numbers + 1):
        sum += i
    print ("Сумма чисел от", number, "до", numbers, "равна:", sum)
else:
    print (f"{number} больше {numbers} ")