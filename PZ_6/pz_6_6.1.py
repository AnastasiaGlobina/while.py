# Даны целые числа N (>2), A и B. Сформировать и вывести целочисленный список
# размера 10, первый элемент которого равен A, второй равен B, а каждый
# последующий элемент равен сумме всех предыдущих.
def generate_list (N, A, B):
    result = [A, B]
    for i in range(2, N):
        result.append(result[i-1] + result[i-1])
        return result
N=10
A=3
B=5
output_list = generate_list (N, A, B)
print(output_list)