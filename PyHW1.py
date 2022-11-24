# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# day = int(input("Enter number from 1 to 7: "))

# if day == 6 or day == 7:
#     print("Hey, it's weekend")
# else:
#     print("No, go to work")

# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ⋀ - and ⋁ - or ¬ - not

# x = 0
# y = 0
# z = 0

# for x in range (2):
#     print(x, y, z)
#     d = not (x or y or z) == (not x) and (not y) and (not z)
#     print(d)

#     for y in range (2):
#         print(x, y, z)
#         d = not (x or y or z) == (not x) and (not y) and (not z)
#         print(d)
    
#         for z in range (2):
#             print(x, y, z)
#             d = not (x or y or z) == (not x) and (not y) and (not z)
#             print(d)


    

# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input("Enter x not equal to 0: "))
# y = int(input("Enter y not equal to 0: "))

# if x == 0 or y == 0:
#     print("Wrooong, do it again!")

# elif x > 0 and y > 0:
#     print ("1st quarter")

# elif x > 0 and y < 0:
#     print ("4nd quarter")

# elif x < 0 and y < 0:
#     print ("3rd quarter")

# else:
#     print("2th quarter")


# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

# q = int(input("Enter quarter: "))

# if q == 0 or q > 4:
#     print("Wrooong, do it again!")

# elif q == 1:
#     print ("x > 0, y > 0")

# elif q == 4:
#     print("x > 0, y < 0")

# elif q == 3:
#     print("x < 0, y < 0")

# else:
#     print("x < 0, y > 0")

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Я загуглила, как искать квадратный корень в Питоне, нагуглила вот это. 
# Брат потом объяснил, что это через "импортирование библиотеки", я пока плохо опнимаю, что это значит.
# Но надеюсь, пойдет. Зато работает :)

# import math

# x1 = int(input("Enter x1: "))
# y1 = int(input("Enter y1: "))
# x2 = int(input("Enter x2: "))
# y2 = int(input("Enter y2: "))

# d = math.sqrt((x2 - x1)**2 + (y2 - y1 )**2)

# print("Distance is ", d)