# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# day = int(input("Enter number from 1 to 7: "))

# if day == 6 or day == 7:
#     print("Hey, it's weekend")
# else:
#     print("No, go to work")

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ⋀ - and ⋁ - or ¬ - not

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
#     print ("2nd quarter")

# elif x < 0 and y < 0:
#     print ("3rd quarter")

# else:
#     print("4th quarter")


# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

# q = int(input("Enter quarter: "))

# if q == 0 or q > 4:
#     print("Wrooong, do it again!")

# elif q == 1:
#     print ("x > 0, y > 0")

# elif q == 2:
#     print("x > 0, y < 0")

# elif q == 3:
#     print("x < 0, y < 0")

# else:
#     print("x < 0, y > 0")

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21