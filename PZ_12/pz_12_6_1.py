#1.Даны температуры за месяц март. Необходимо найти количество
#положительных и отрицательных значений температур в месяце, самую низкую и
#самую высокую температуры, а также среднемесячное значение температуры.
import random
temperatures = [random.randint(-10,30) for _ in range(31)]
print("Температуры за месяц:",temperatures )
p_temperatures = len([temp for temp in temperatures if temp>0])
o_temperatures = len([temp for temp in temperatures if temp<0])
min_temp = min(temperatures)
max_temp = max(temperatures)
s_temp = sum(temperatures)/len(temperatures)
print("Положительные температуры:",p_temperatures)
print("Отрицательные температуры:", o_temperatures)
print("Минимальная температура:", min_temp)
print("Максималная температура:", max_temp )
print("Среднее значение температуры:", s_temp )
print("Среднее значение температуры:", s_temp )