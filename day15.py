
# #2
# while True:
#     unicode = input('Введите символ юникод:')
#     if unicode == '0':
#         break
#     else:
#         print(unicode)
#6
x = """
The ZEN OF Python, BY Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those! """

# def Zaglav(x):
#     t_words = []
#     with open('homew.txt', 'w') as k:
#         w = k.write(x)
#
#     with open('homew.txt', 'r') as l:
#         words = l.read().split()
#         for word in words:
#             if word.isupper() == True:
#                 t_words.append(word)
#     print(t_words)
#     pass
# Zaglav(x)
# #7
# def C_or_c(x):
#     t_words = []
#     with open('python.txt', 'w') as k:
# 	    w = k.write(x)
#     with open('python.txt', 'r') as l:
# 	    words = l.read().split()
# 	    for word in words:
# 		    if 'c' in word or word[0] == 'C':
# 			    t_words.append(word)
#     print(t_words)
# C_or_c(x)

# #15
# def bank(a,years):
#     total = 0.0
#     for i in range(years):
#         total = total + a
#         if i%1 == 0:
#             a = a*1.1
#             total = total*1.1
#     print(round(total,2))
# bank(100,3)
#14
def season(month):
    if month == 12 and month < 3:
        print('winter')
    elif month >= 2 and month < 6:
        print('spring')
    elif month >5  and month < 9:
        print('summer')
    elif month > 8 and month < 12:
        print('autumn')
    else:
        print('Месяца с таким порядковым номеров нет')
season(2)
##13
# lst = [-5,-3,-2, 10, 9, 22, 44]
# lst1 = []
# lst2 = []
# for i in lst:
#     if i > 0:
#         lst1.append(i)
#     elif i < 0:
#         lst2.append(i)
# print(lst1)
# print(lst2)

##16
# ls = []
# while True:
#     a = float(input('Введите температуру измерения за сутки:'))
#     if a < -273.15:
#         break
#     ls.append(a)
# print(sum(ls) / len(ls))
# #1
# import random
# a = random.randint(0,10)
# for x in range(3):
#     guess = int(input('Угадай число от 0 до 11!: '))
#     if guess == a:
#         print('Молодец ты отгадал!,число было: ',a)
#         exit()
# print('Ты не смог отгадать число:',a)

# #3
# stroka = input('Напишите строку: ')
# if 10 > len(stroka):
#     x = 10 - len(stroka)
#     stroka = stroka + (x*'*')
#     print(stroka)
# elif len(stroka) > 10:
#     print('Ваша строка длинее 10 символов!')

# #4
# max = 0
# numbers = []
# for x in range(6):
#     num = float(input('input float num: '))
#     numbers.append(num)
# min = numbers[0] + 1
# for x in numbers:
#     if min > x:
#         min = x
#     if max < x:
#         max = x
# print('max number: ',round(max,2), 'min number: ', round(min,2))

# #5
# a = input('')
# x = list(a)
# min = int(x[0]) + 1
# max = 0
# for k in x:
#     if int(k) < min:
#         min = int(k)
#     if int(k) > max:
#         max = int(k)
# print(max, min)

# #9
# a = int(input('Первый аргумент: '))
# b = int(input('Второй аргумент: '))
# def func1(x,y):
#     a = x*y
#     def func2(x,y):
#         b = x/y
#         print(a + b)
#     func2(x,y)
# print(func1(a,b))

# #10
# text = "The Zen of Python, by Tim PetersBeautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one--and preferably only one -- obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"
# text1 = text.split(' ')
# print(text)
# p_words = []
# def filter(x):
#     if 'p' in x:
#         return True
#     else:
#         return False
# for x in text1:
#     if filter(x) == True:
#         p_words.append(x)
# print(p_words)

# #11
# dict_one = {'a':1, 'b':2, 'c':3}
# dict_two = {'d':4, 'e':5, 'f':6}
# dict_three = {'g':7, 'h':8, 'i':9}
# dict_four = {}
# dict_four.update(dict_one)
# dict_four.update(dict_two)
# dict_four.update(dict_three)
# print(dict_four)

# #12
# import collections
# user_input = input('Напиши че нибудь cлитно суранам братан! ')
# n = int(input('На сколько сдвигов хотите? '))
# a_list = collections.deque(list(user_input))
# a_list.rotate(n)
# result = list(a_list)
# print(result)





