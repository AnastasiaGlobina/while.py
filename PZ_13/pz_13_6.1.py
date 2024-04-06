#1. В матрице элементы первого столбца возвести в куб.
import random
matrix = [[random.randint(1,10) for _ in range(3)] for _ in range(3)]
print("Исходная матрица:")
for row in matrix:
    print(row)
new_matrix = [[col **3 if idx == 0 else col for idx,col in enumerate(row)] for row in matrix]
print("\n Исходная матрица:")
for row in new_matrix:
    print(row)
