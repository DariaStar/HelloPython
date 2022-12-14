# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

# something = [2, 3, 5, 9, 3]

# def summa(anylist):
#     i = 1
#     s = 0
#     while i < len(anylist):
#         s += anylist[i]
#         i += 2
#     print(s)
        
# summa(something)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# something1 = [2, 3, 4, 5, 6]
# something2 = [2, 3, 5, 6]

# def proisv (anylist):
#     i = 0
#     while i < len(anylist) / 2:
#         p = anylist[i] * anylist[len(anylist) - 1 - i]
#         print(f"{anylist[i]} * {anylist[len(anylist) - 1 - i]} = {p}")  
#         i += 1

# proisv(something1)
# print()
# proisv(something2)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

# somethingborrowed = [1.1, 1.2, 3.1, 10.01]
# somethingnew = []
# i = 0

# while i < len(somethingborrowed):
#     dp = somethingborrowed[i] % 1
#     somethingnew.append((round(dp, 2)))
#     i += 1

# print(max(somethingnew) - min(somethingnew))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Enter number: '))
# l = []

# def binar (x, y):
#     while x > 0:
#         a = str(x % 2)
#         y.append(a)
#         x = x // 2
#     y.reverse()
#     print(" ".join(y))

# binar(n, l)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# k = int(input("Enter number: "))
# lneg = [1, -1]
# lpos = [0, 1, 1]

# def fib_pos(k, lpos):
#     i = 0
#     f1 = 1
#     f2 = 1
#     while i < k - 2:
#         fsum = f1 + f2
#         f1 = f2
#         f2 = fsum
#         lpos.append(f2)
#         i += 1
#     return lpos   
 
# def fib_neg(k, lneg):
#     f1 = 1
#     f2 = -1
#     i = 0
#     while i < k - 2:
#         fsum = f1 - f2
#         f1 = f2
#         f2 = fsum
#         lneg.append(f2)
#         i += 1
#     lneg.reverse()
#     return lneg   

# fib_neg(k, lneg)
# fib_pos(k, lpos)
# print(lneg + lpos)
