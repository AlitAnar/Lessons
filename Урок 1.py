"""
1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

print(f"5 & 6 = {5 & 6}")
print(f"5 | 6 = {5 | 6}")
print(f"5 ^ 6 = {5 ^ 6}")
print(f"5 >> 1 = {5 >> 2}")
print(f"5 << 2 = {5 << 2}")

"""
2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b ,
проходящей через эти точки.
"""

print("Введите координаты двух точек прямой")
x1, y1 = [float(itr) for itr in input("Введите координаты первой точки в формате x y: ").split(" ")]
x2, y2 = [float(itr) for itr in input("Введите координаты второй точки в формате x y: ").split(" ")]

k = (y2 - y1)/(x2 - x1)
b = y2 - (k * x2)

print(f"y = {k}x + {b}")
print(f"{k * x1 + b} = k*x1 + b")
print(f"{k * x2 + b} = k*x2 + b")

"""
3. Написать программу, которая генерирует в указанных пользователем границах:
    a. случайное целое число,
    b. случайное вещественное число,
    c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
включительно.
"""

from random import randint
from random import uniform

print("Введите границы диапазона")
a = input("Введите левую границу: ")
b = input("Введите правую границу: ")

if a.isalpha() and b.isalpha():
    a_code, b_code = ord(a.lower()), ord(b.lower())
    if b_code < a_code:
        a_code, b_code = b_code, a_code
    c = chr(randint(a_code, b_code))
elif a.isdecimal() and b.isdecimal():
    a, b = int(a), int(b)
    if b < a:
        a, b = b, a
    c = randint(a, b)
else:
    a, b = float(a), float(b)
    if b < a:
        a, b = b, a
    c = uniform(a, b)

print(f"Случайное значение: {c}")

"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и
сколько между ними находится букв.
"""

print("Введите две буквы")
a = input("Первая буква: ").lower()
b = input("Вторая буква: ").lower()

a_num = ord(a) - ord("a") + 1
b_num = ord(b) - ord("a") + 1
dist = 0 if a_num == b_num else abs(a_num - b_num) - 1

print(f"Буква '{a}' на {a_num} месте.\n"
      f"Буква '{b}' на {b_num} месте.\n"
      f"Между '{a}' и '{b}' {dist} букв")