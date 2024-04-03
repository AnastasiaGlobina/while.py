#2. Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
import random
matrix = [[random.randint(1,20) for _ in range(3)] for _ in range(3)]
print("Исходная матрица:")
for row in matrix:
    print(row)
for i in range(3):
    for j in range(3):
        if matrix[i][j] > 10:
            matrix[i][j] =0
print('\nИтоговая матрица:')
for row in matrix:
    print(row)