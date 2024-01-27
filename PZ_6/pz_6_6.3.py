# Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
# список вправо на K позиций (при этом A1 перейдет в AK+1, A2 — в AK+2, ..AN-K — в
# AN, а исходное значение K последних элементов будет потеряно). Первые K
# элементов полученного списка положить равными 0.
def shift_elements(arr, k):
    n = len(arr)
    k = k%n
    shifted_arr =[0]*k
    for i in range(n-k):
        shifted_arr.append (arr[i])
    return shifted_arr
input_list =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k=3
result =shift_elements(input_list, k)
print("Результат: ", result)