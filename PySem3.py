# 1. Реализуйте алгоритм задания случайных чисел
# без использования встроенного генератора псевдослучайных чисел.

# import time

# def ran ():   
#     t = time.time()
#     print(round(t % 10))

# ran()

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['sdf13', 'fds66', '34']
# -> 3
# 'sdf13', '34'

# list_ = ['sdf13', 'fds66', '34']  #красиво, но не работает
# elem = input("Enter symbol to find: ")

# def find(givenlist, elem):
#     for i in givenlist:
#         a = list(i)
#         print (a)
#         for j in a:
#             if a[j] == elem:
#                 print("присутсвует")
#             else:
#                 print("nyet")

# find(list_, elem)

# list_ = ['sdf13', 'fds66', '34']  #красиво, но не работает
# elem = input("Enter symbol to find: ")

# def in_list(anylist, elem):
#     for i in range(len(anylist)):
#         if elem in anylist:
#             print(list[i])

# print(in_list(list_, elem))


# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# mylist = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# elem = "qwe"
# result = False

# def in_list(list_, find_):
#     result = False
#     for i in list_:
#         if find_ in i:
#             result = True
#         print(i)
#     return result

# def func_1():
#     list_a = ["123", "234", 123, "567"]
#     find_char = "123"
#     new_list = []
#     for i in range(len(list_a)):
#         if find_char == list_a[i]:
#             new_list.append(i)
#             if len(new_list) <= 1:
#                 return -1
#     return new_list[1]

# print(func_1())

# def fun():
#     list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
#     a = input('Введите число - ')
#     count = 0
#     for k in range(len(list)):
#         if list[k] == a:
#             count += 1
#             if count == 2:
#                 return k
#         return -1

# print(fun())