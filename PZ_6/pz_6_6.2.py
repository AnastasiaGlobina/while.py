# Дан список размера N. Найти максимальный из его локальных минимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).
import random


def find_local_minima(arr):
    local_minima = []
    for i in range (1,len (arr) -1):
        if arr [i] < arr [i-1] and arr [i] < arr [i+1]:
            local_minima.append(arr[i])
    if len (local_minima) ==0:
        return "В списке нет локальных минимумов"
    else:
        return max(local_minima)
input_list = [random.randint(1, 100) for _ in range(10)]
result = find_local_minima(input_list)
print ("Максимальный из локальных минимумов: ", result)