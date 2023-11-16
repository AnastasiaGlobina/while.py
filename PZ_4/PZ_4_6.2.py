number = int(input ("введите целлое число: "))
digits = []
while number >0:
    digit = number % 10
    digits.insert (0, digit)
    number //=10
for digit in digits:
    print (digit)
