# Вычислить число c заданной точностью d.

# d = float(input())
# num = float(input())
# s = str(d)
# if '.' in s:
#     d = abs(s.find('.') - len(s)) - 1
# else:
#     print('Не корректные данные')
# print(round(num, d))


# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# n = int(input('Введите число: '))
# p = 2
# a = []
# while n >= 2:
#     if n % p == 0:
#         n = n / p
#         a.append(p)
#     else:
#         p +=1
# print(a)

# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности.

# a = []
# a = [int(i) for i in input('Введите последовательность чисел через пробел: ').split()]
# print(a)
# b = []
# b.append(a[0])
# for idx in range(len(a) - 1):
#     if a[idx] != a[idx + 1]:
#         b.append(a[idx + 1])
# print(b)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# def create_list(size):
#     new_list = [0]*size
#     for i in range(len(new_list)):
#         new_list[i] = int(input("Введите число: "))
#     return new_list


# def show_uniq_num(array):
#     new_unic_list = set(array)
#     res_array = list(new_unic_list)
#     return res_array


# try:
#     list_size = int(input("Введите размер последовательноси: "))
#     start_list = create_list(list_size)
#     print('Исходная последовательность: ')
#     print(' '.join(map(str, start_list)))

#     result_list = show_uniq_num(start_list)
#     print("Список неповторяющихся элементвов в исходной последовательности: ")
#     print(' '.join(map(str, result_list)))
# except:
#     print('Введите число')


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint, random


# def create_ratio_list(num):
#     ratio = []
#     while num > 0:
#         ratio.append(randint(0, 100))
#         num -= 1
#     return ratio

# def save(str):
#     with open('Многочлен.txt', "w") as data:
#         data.write(str)
#         print('Запись прошла успешно!')

# def create_polynomial(ratio_list, k):
#     polynomial = []

#     for i in range(len(ratio_list)):
#         if ratio_list[i] == 0:
#             continue
#         elif ratio_list[i] == 1:
#             polynomial.append('x')
#             if k == 1:
#                 polynomial.append(' + ')
#             else:
#                 polynomial.append('^')
#                 polynomial.append(k)
#                 polynomial.append(' + ')
#                 k -= 1
#         else:
#             polynomial.append(ratio_list[i])
#             polynomial.append('x')
#             if k != 1:
#                 polynomial.append('^')
#                 polynomial.append(k)
#                 polynomial.append(' + ')
#                 k -= 1
#             else:
#                 polynomial.append(' + ')

#     polynomial.append(randint(0, 100))

#     if polynomial[-1] == 0:
#         polynomial.remove(0)
#         polynomial.remove(' + ')
#     polynomial.append(' = 0')
#     return polynomial


# try:
#     print("Cоздание случайного многочлена")
#     k = int(input("Задайте натуральную степень 'k': "))
#     if k > 0:
#         ratio_array = create_ratio_list(k)
#         result_polymomial = create_polynomial(ratio_array, k)
#         result_string = ''.join(map(str, result_polymomial))
#         save(result_string)
#     else:
#         exit()
# except:
#     print("Введите целое число 'k' > 0")

