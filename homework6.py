# # Задача 1. Создайте программу для игры в "Крестики-нолики".

# table = list(range(1,10))

# def draw_table(table):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", table[0+i*3], "|", table[1+i*3], "|", table[2+i*3], "|")
#         print ("-" * 13)

# def user_input(player_step):
#     valid = False
#     while not valid:
#         player_answer = input("Где рисуем " + player_step + " ? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Неправильный ввод! Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(table[player_answer-1]) not in "XO"):
#                 table[player_answer-1] = player_step
#                 valid = True
#             else:
#                 print ("Сюда нельзя, - клетка уже занята...")
#         else:
#             print ("Неправильный ввод! Введите число от 1 до 9 чтобы походить.")

# def check_win(table):
#     win_combo = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for i in win_combo:
#         if table[i[0]] == table[i[1]] == table[i[2]]:
#             return table[i[0]]
#     return False

# def main(table):
#     counter = 0
#     win = False
#     while not win:
#         draw_table(table)
#         if counter % 2 == 0:
#             user_input("X")
#         else:
#             user_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(table)
#             if tmp:
#                 print (f'Поздравляю! - {tmp} Выиграл!')
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_table(table)

# main(table)


# # Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# # Пример: 2+2 => 4;
# #         1+2*3 => 7;
# #         1-2*3 => -5;
# # Добавьте возможность использования скобок, меняющих приоритет операций.
# # Пример: 1+2*3 => 7;
# #         (1+2)*3 => 9;

# task = input('Введите пример: ')
# #task = '11+2*3-1'
# #task = '17 - 5 * 6 / 3 - 2 + 4 / 2'
# #task = '9 - 2 * 3 / 3 - 2 + 4 / 2'
# #task = '17 - 5 * 6 - 2 + 4 / 2'
# #task = '1 - 2*3'

# task = task.replace(' ', '')
# print(task)

# def mult(task):
#     a = task.index("*")
#     answer = int(task[a-1]) * int(task[a+1])
#     if len(task) == 3:
#         task = str(answer)
#     else:
#         task = task[0:a-1] + str(answer) + task[a+2:]
#     return task

# def div(task):
#     a = task.index("/")
#     answer = int(task[a-1]) // int(task[a+1])
#     if len(task) == 3:
#         task = str(answer)
#     else:
#         task = task[0:a-1] + str(answer) + task[a+2:]
#     return task

# def sum(task):
#     a = task.index("+")
#     answer = int(task[a-1]) + int(task[a+1])
#     if len(task) == 3:
#         task = str(answer)
#     else:
#         task = task[0:a-1] + str(answer) + task[a+2:]
#     return task

# def diff(task):
#     a = task.index("-")
#     answer = int(task[a-1]) - int(task[a+1])
#     if len(task) == 3:
#         task = str(answer)
#     else:
#         task = task[0:a-1] + str(answer) + task[a+2:]
#     return task

# if '*' in task:
#     counter = task.count('*')
#     if counter > 1:
#         for i in range(counter):
#             task = mult(task)
#     else: 
#         task = mult(task)
#     #print(task)

# if '/' in task:
#     counter = task.count('/')
#     if counter > 1:
#         for i in range(counter):
#             task = div(task)
#     else: 
#         task = div(task)
#     #print(task)

# if '+' in task:
#     counter = task.count('+')
#     if counter > 1:
#         for i in range(counter):
#             task = sum(task)
#     else: 
#         task = sum(task)
#     #print(task)

# if '-' in task:
#     counter = task.count('-')
#     if counter > 1:
#         for i in range(counter):
#             task = diff(task)
#     else: 
#         task = diff(task)
#     print(task)
