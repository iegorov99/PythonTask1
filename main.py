'''
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

# import sys

# try :
#     a = int(input('Введите число: '))
# except ValueError :
#     print('Это не число')
#     sys.exit()

# if a < 0 :
#     a = abs(a)
# b = 0
# while a > 0 :
#     b += a%10
#     a//=10
# print('Сумма цифр введённого числа равна', b)

'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
'''

# import sys

# try :
#     s = int(input('Введите общее количество журавликов: '))
# except ValueError :
#     print("Это не число")
#     sys.exit()

# if s % 6 == 0:
#     p = (s+1) // 6
#     k = 4 * p
#     c = p
#     print ('Петя сделал', p, 'журавликов')
#     print('Катя сделала', k , 'журавликов')
#     print('Сережа сделал', c, 'журавликов')
# else:
#     print('С введённым количеством журавликов нарушается условие задачи')

'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no
'''

# import sys

# try :
#     ticket = [int(input('Введите цифру билета: ')) for i in range(6)]
# except ValueError:
#     print('Это не число')
#     sys.exit()

# for i in ticket:
#     if i > 9  or i<0:
#         print('Неверный формат билета')
#         sys.exit()

# a = ticket[0] + ticket[1] + ticket[2]
# b = ticket[3] + ticket[4] + ticket[5]
# if a == b :
#     print('Билет с номером', ticket, '– счастливый')
# else :
#     print('Билет с номером', ticket, '– не счастливый')

'''
Задача 8: Требуется определить, можно ли от шоколадки размером n на m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
'''
# import sys

# try:
#     n = int(input('Введите колчество долек в длину: '))
#     m = int(input('Введите колчество долек в ширину: '))
#     if n == m == 1:
#         print('Отламывать нечего')
#         sys.exit()
#     k = int(input('Введите колчество долек которое хотет отломить одним разломом: '))
# except ValueError:
#     print('Это не число')
#     sys.exit()


# if n == 1 or m ==1:
#     if n == 1 :
#         if k < m :
#             print('Можно')
#         else :
#             print('Нельзя')
#     else :
#         if k < n :
#             print('Можно')
#         else :
#             print('Нельзя')
# elif n == m :
#     if k >= n and k % n == 0 and k < n * m :
#         print('Можно')
#     else :
#         print('Нельзя')
# elif k % n == 0 or k % m ==0 and  k< n * m :
#     print('Можно')
# else :
#     print('Нельзя')
