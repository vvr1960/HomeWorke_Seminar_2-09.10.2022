# 1.	Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
#       Пример:
#       - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


import math

n = int(input('Введите значение n: '))
Lst_key = []
for i in range(1, n +1):
    Lst_key.append(i)
lst_num = [math.ceil((1+1/i)**i) for i in range(1, n+1)]

Lst_sum = []
sum_num = 0
for j in lst_num:
    sum_num += j
    Lst_sum.append(sum_num)
Sum_Dict = dict(zip(Lst_key, Lst_sum))
print()
print(f' Список последовательности c округлением\n до ближайшего большего целого числа: {lst_num}')
print()
print(f'Значения сумм элементов: {Sum_Dict}')
