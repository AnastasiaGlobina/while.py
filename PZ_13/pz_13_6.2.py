#2. Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
import random
matrix = [[random.randint(1,20) for _ in range(3)] for _ in range(3)]
print("Исходная матрица:")
for row in matrix:
    print(row)
new_matrix = [[0 if x > 10 else x for x in row] for row in matrix]
print('\nИтоговая матрица:')
for row in new_matrix:
    print(row)