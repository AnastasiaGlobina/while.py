#Код разбивает введенное пользоавателем число на отдельные цифры и выводит их в обратном порядке
try:
    number = int(input("введите целое число: "))
    while number > 0:
        digit = number % 10
        print(digit)
        number = number//10
except ValueError:
    print("Вы ввели не чило, попытайтесь ввести цифры!")
