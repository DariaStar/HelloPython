# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 0,56 -> 11

# n = str(input("Enter real number: "))
# l = list(n)
# for j in range (len(l) - 1):
#     if l[j] == ',':
#         l.remove(l[j])
# i = 0
# sum = 0
# while i < len(l):
#     k = int(l[i])
#     sum += k
#     i += 1
# print(sum)

#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Enter number: "))
# i = 1 
# res = 1

# while i < n + 1:
#     res = res * i
#     print(res, end=" ")
#     i += 1


#3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# n = int(input("Enter number: "))
# i = 1
# sum = 0
# while i < n + 1:
#     d = (1 + 1/i)**i
#     print(round(d, 2))
#     sum += d
#     i += 1
# print("The sum is", round(sum, 2))


#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел

# n = int(input("Enter number: "))
# l1 = list()
# for i in range(-n, n + 1, 1):
#     l1.append(i)
# print(l1)

# i = str(input("Enter indexes, devided by spaces: "))
# l2 = i.split(" ")
# res = 1
# for k in range(len(l2)):
#     r = int(l1[k])
#     res *= r
#     k += 1
# print(res)

# Реализуйте алгоритм перемешивания списка.
# Первая моя задумка перемешивает, нонекоторые эелементы повторяются, а нектороые наоборот не используются:

# i = str(input("Enter elenets, devided by spaces: "))
# l = i.split(" ")
# print(l)
# import random
# for i in range(len(l)):
#     l[i] = l[random.randrange(0, len(l))]
# print(l)

#Вторая простая, но неинтересная:

# i = str(input("Enter elenets, devided by spaces: "))
# l = i.split(" ")
# print(l)
# import random
# random.shuffle(l)
# print(l)

#Третья вот такая:

# i = str(input("Enter elenets, devided by spaces: "))
# l = i.split(" ")
# print(l)
# for i in range(0, len(l) - 2, 2):
#     k = l[i]
#     l[i] = l[i + 2]
#     l[i + 2] = k
#     i += 1
# for i in range(0, len(l) - 2, 1):
#     k = l[i]
#     l[i] = l[i + 2]
#     l[i + 2] = k
#     i += 1
# print(l)