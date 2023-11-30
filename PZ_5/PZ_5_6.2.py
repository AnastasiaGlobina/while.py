#Описать функцию InvertDigits(K), меняющую порядок следования цифр целого
#положительного числа K на обратный (K — параметр целого типа, являющийся
#одновременно входным и выходным). С помощью этой функции поменять порядок
#следования цифр на обратный для каждого из пяти данных целых чисел.
def Digits(K):
    reversed_number = 0
    while K > 0:
        digit = K %10
        reversed_number = (reversed_number*10) + digit
        K//=10
        return reversed_number
numbers = [12,45,67,90,23]
for num in numbers:
    reversed_num = Digits(num)
    print (reversed_num)