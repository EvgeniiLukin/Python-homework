# Задайте список из нескольких чисел.  Напишите программу, 
# которая найдёт сумму  элементов списка, стоящих на нечётной позиции.


# a = []
# a = [int(i) for i in input('Введите массив через пробел: ').split()]
# print(a)
# i = 1
# sum = 0
# while i < len(a):
#     sum += a[i]
#     i +=2
# print(sum)



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# try:
#     len = int (input('Введите длину списка: '))
#     list = []
#     list2 =[]
#     for i in range (len):
#         list.append (int(input(f'Введите {i + 1} число: ')))
#     print()
#     print(f'Список: {list}')

#     if len % 2 == 0:
#         len = int(len / 2)
#     else:
#         len = int((len / 2) + 1)

#     for i in range(len):
#         list2.append (list[i] * (list [-1 - i]))
#     print(f'Произведение пар: {list2}')
# except:
#     print('Введите целое число!')


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5, 10.01]

# for i in range(5):
#     list[i] = round(list [i] - int(list[i]), 4)
# print (list)

# max = list[0]
# min = list[0]

# for i in range(5):
#     if list[i] > max:
#         max = list [i]
        
#     if list[i] < min and list[i] !=0:
#         min = list [i]
        
# print(f'Разница между максимальным и минимальным значением дробной части элементов = {max-min}')


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# try:
#     def dvoichnaya(num):
#         if num == 0:
#             return 0
#         else:
#             list = []
#             while num >= 1:
#                 list.insert(0, int(num % 2))
#                 num = num / 2
#             return list    
 
#     num = float (input('Введите число: '))
   
#     print(*dvoichnaya(num))
# except:
#     print('Введите число')


# Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке


# try:
#     size = int(input('Введите количество чисел в списке: '))
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))

#     list = [num1, num2]
#     for i in range(size - 2):
#         list.append(list[i]+list[i + 1])
#     print(f'Список чисел Фибоначчи: {list}')
# except:
#     print('Введите число')