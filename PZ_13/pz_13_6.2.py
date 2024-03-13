#2. Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
import numpy as np
matrix = np.random.randint(1,20, size=(3,3))
print('Исходная матрица:')
print(matrix)
matrix = np.where(matrix > 10, 0, matrix)
print('\nИтоговая матрица:')
print(matrix)