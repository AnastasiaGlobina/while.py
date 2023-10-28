print("Свод операций доступных на калькуляторе")
print("+   сложение ")
print("-  вычитание")
print("*  умножение")
print("/  деление")
print("//  деление нацело")
operation = input("Введите операцию; ( + ,-, * или / ): ")
numbers_1 = int(input ("введите первое число: "))
numbers_2 = int(input ("Введите второе число: "))
if operation == "+":
    result = numbers_1 + numbers_2
elif operation == "-":
    result = numbers_1 - numbers_2
elif operation == "*":
    result = numbers_1 * numbers_2
elif operation == "/":
    result = numbers_1 / numbers_2
elif operation == "//":
    result = numbers_1 // numbers_2
print ("Результат:", result)
