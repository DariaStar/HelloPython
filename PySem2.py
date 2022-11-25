# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 
#         1, -3, 9, -27, 81
#         1, -3, 9, -27, 81
#         (-3)**0 (-3)**1 (-3)**2 (-3)**3 (-3)**4


# n = int(input('Введите число n - '))
# for x in range(n):
#     resalt = (-3)**x
#     print(resalt, end=' ')


# Моржовый оператор
# while x:=int(input('--> ')) < 0:
#     print('Введи число больше нуля')

# n = int(input('Input number: '))
# i = 1
# while i < n + 1:
#     print(3*i + 1, end= ' ')
#     i += 1

# 2)
# def dict_comprehension() -> dict:
#     try:
#         n = int(input('Введите целое число >=0:'))
#         if n > 0:
#             # Генератор словаря(dict_comprehension)
#             dict = {k: (3 * k + 1) for k in range(1, n)}
#             print(f'- Для n = {n}: {dict} ')
#             # Возвращает словарь
#             return dict
#         # Возвращает пустой словарь, так условие
#         return {}
#     except ValueError:
#         print('Вы ввели не целое число!')
#         print('Повторите ввод')
#         return dict_comprehension()
# dict_comprehension()

# 3. Напишите программу, в которой пользователь будет задавать 
# две строки, а программа - определять количество вхождений одной строки в другой.
# 'Я люблю Python'
# 'лю'
#1)
# str1 = 'Я люблю Python'
# str2 = 'лю'

# print (str1.count(str2))
#2)

# test_str = str(input())
# counter = test_str.count(str(input())) 
 
# print ("Count is : " +  str(counter))


# 3)
# text = 'Я люблю Python люблю'
# searchText = input('Введите строку для подсчета вхождения: ')

# list = text.split(searchText)
# print(len(list)-1)

# 4)
# my_string = 'Я люблю Python'
# s2 = input("Введите строку для проверки вхождения: ")
# number = 0
# for i in range(len(my_string) - len(s2)+1):
#     if my_string[i:i+len(s2)] == s2:
#         number += 1
# print(number)
