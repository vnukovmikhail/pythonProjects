# Разработай функцию, которая возвращает количество цифр
# в заданной строке символов.
#
# s = input()
#
# i = 0
# for el in s:
#     try:
#         int(el)
#         i+=1
#     except ValueError:
#         pass
#
# print(i)



# Разработай процедуру, которая выводит символы строки в
# обратном порядке.
#
# s = input()
# r = ''
# for el in s:
#     r = el + r
#
# print(r)




#Разработай логическую функцию, которая определяет, содержится ли в строке буква 'a'.
# s = input()
# a = 0
# for el in s:
#     print(el)
#     if (el == 'а') or (el == 'a'):
#         a+=1
#
# if a == 0:
#     print('нет а')
# else:
#     print(f'найденно {a} букв а')




# С клавиатуры считывается текст. Разработай алгоритм,
# который определяет, содержатся ли в строке только буквы и
# символ '.'.
# s = input()
# y = False
# for el in s:
#     if el in ['0','1','2','3','4','5','6','7','8','9', '.']:
#         y = True
#     else:
#         y = False
#         break
#
# if y == 0:
#     print('ну нет и нет, чего горевать')
# else:
#     print('опа есть, это нам подходит')