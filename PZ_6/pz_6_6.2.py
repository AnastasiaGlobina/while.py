# Дан список размера N. Найти максимальный из его локальных минимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).
import random
def local_minima(arr):
    minima = []
    for i in range (1,len (arr) -1):
        if arr [i] < arr [i-1] and arr [i] < arr [i+1]:
            minima.append(arr[i])
    if len (minima) == 0:
        return "В списке нет локальных минимумов"
    else:
        return max(minima)
numbers = [random.randint(1, 100) for _ in range(10)]
print ("Исходный список: ", numbers)
result = local_minima(numbers)
print ("Максимальный из локальных минимумов: ", result)