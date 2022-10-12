# Задача 5.	Реализуйте алгоритм перемешивания списка.

from random import randint

N = int (input('Введите число N: '))
Lst = []
for i in range(N):
    Lst.append(randint(-N, N))
print(f'Исходный список:     {Lst}')

for i in range(len(Lst) - 1, 0, -1):
    j = randint(0, i + 1)
    Lst[i], Lst[j] = Lst[j], Lst[i]
print(f'Перемешанный список: {str(Lst)}')
