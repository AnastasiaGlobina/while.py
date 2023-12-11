# Даны целые числа N (>2), A и B. Сформировать и вывести целочисленный список
# размера 10, первый элемент которого равен A, второй равен B, а каждый
# последующий элемент равен сумме всех предыдущих.
def generate_list (A, B):
    result = [A, B]
    for i in range(10):
        N = sum(result)
        result.append(N)
    return result
A=3
B=5
output_list = generate_list (A, B)
print(output_list)