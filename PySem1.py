#1. Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да      ctrl+? - за/раскомментировать
# - 8,9 -> нет

# a = int(input("Enter number: "))                       
# b = int(input("Enter number: "))

# if a*a == b or b*b == a:
#     print("yes")
# else:
#     print("no")

#     тернарный оператор a = 2 if (num_1 == mum_2) else 4

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# a = []
# for _ in range(5):
#     k = int(input("Enter number: "))
#     a.append(k)

# max = a[0]

# for i in range (5):
#     if a[i] > max:
#         max = a[i]

# print(max)

# range(start, stop, step)
# range(5) -> [0, 1, 2, 3, 4]
# range(2, 5) -> [2, 3, 4]
# range(1, 7, 2) -> [1, 3, 5]

# range(len(a))


# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# *Примеры:*

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# num = int(input("Введите число: "))
# for i in range(-num, num+1):
#     print(i, end=' ')

# 4. Напишите программу, которая будет принимать на вход дробь и
# показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 0,34 -> 3

# n = float(input('Input number: '))
# if int(n) == n:
#     print('no')
# else:
#     print(int(n * 10) % 10)

5.

x = int(input('--> '))
if (((x % 5 == 0) and (x % 10 == 0)) or (x % 15 == 0)) and (x % 30 != 0):
    print(True)