#1. В матрице элементы первого столбца возвести в куб.
import random
matrix = [[random.randint(1,10) for _ in range(3)] for _ in range(3)]
print("Исходная матрица:")
for row in matrix:
    print(row)
for i in range(3):
    matrix[i][0] = matrix[i][0] ** 3
print("\n Исходная матрица:")
for row in matrix:
    print(row)