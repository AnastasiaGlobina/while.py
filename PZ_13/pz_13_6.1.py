#1. В матрице элементы первого столбца возвести в куб.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    row[0] = row[0] **3
for row in matrix:
    print(row)