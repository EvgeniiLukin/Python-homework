# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

# data = list(map(int,input('Введите числа через пробел: ').split()))
# print(data)
# res = list(filter(lambda x: x >= 10 and x <= 99, data))
# # res = ''.join(map(str, filter(lambda i: 9 < abs(i) < 100, data)))
# print(f'Двухзначные числа: {res}')


# Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]
# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

# data = [12, 'sadf', 5643]
# print(data)
# res = list(filter(lambda x: type(x) == int , data))
# res2 = list(filter(lambda x: type(x) == str, data))
# print(f'Числа: {res}')
# print(f'Строки: {res2}')

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0, 56 -> 11


# data = input('Введите число: ')
# spisok = list(filter(lambda x: x.isdigit(), data))
# spisok = [int(item) for item in spisok]
# print(sum(spisok))

# data = float(input('Введите вещественное число: '))
# data = str(data)
# spisok = list(filter(lambda x: x.isdigit(), data))
# spisok = [int(item) for item in spisok]
# print(sum(spisok))

# data = input('Введите вещественное число: ')
# summa = sum(map(int, data.replace('.','').replace('-','')))
# print(summa)
