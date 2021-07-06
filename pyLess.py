# number = 16
# second_number = []
# first_array = [1, 2, 3]
# second_array = [2, 2]
# # Все, дальше не меняйте
#
# if number > 15:
#     print("1")
#
# if first_array:
#     print("2")
#
# if len(second_array) == 2:
#     print("3")
#
# if len(first_array) + len(second_array) == 5:
#     print("4")
#
# if first_array and first_array[0] == 1:
#     print("5")
#
# if not second_number:
#     print("6")


# знак зодиака

# month = int(input('введите месяц своего рождения'))
# date = int(input('введите дату своего рождения'))
# zodiac = ['овен','телец',',близнецы','рак','лев','дева','весы','скорпион','стрелец','козерог','водолей','рыбы']
#
# if (date>=21 and date<=31 and month==3) or (month==4 and date>=1 and date<=19):
#    print(zodiac[0])
# elif (date>=20 and date<=30 and month==4) or (month==5 and date>=1 and date<=20):
#    print(zodiac[1])
# elif (date>=21 and date<=31 and month==5) or (month==6 and date>=1 and date<=21):
#    print(zodiac[2])
# elif (date>=22 and date<=30 and month==6) or (month==7 and date>=1 and date<=22):
#    print(zodiac[3])
# elif (date>=23 and date<=31 and month==7) or (month==8 and date>=1 and date<=22):
#    print('вы ',zodiac[4])
# elif (date>=23 and date<=31 and month==8) or (month==9 and date>=1 and date<=22):
#    print('вы ',zodiac[5])
# elif (date>=23 and date<=30 and month==9) or (month==10 and date>=1 and date<=23):
#    print('вы ',zodiac[6])
# elif (date>=24 and date<=31 and month==10) or (month==11 and date>=1 and date<=22):
#    print('вы ',zodiac[7])
# elif (date>=23 and date<=30 and month==11) or (month==12 and date>=1 and date<=21):
#    print('вы ',zodiac[8])
# elif (date>=22 and date<=31 and month==12) or (month==1 and date>=1 and date<=20):
#    print('вы ',zodiac[9])
# elif (date>=21 and date<=31 and month==1) or (month==2 and date>=1 and date<=18):
#    print('вы ',zodiac[10])
# elif (date>=19 and date<=29 and month==2) or (month==3 and date>=1 and date<=20):
#    print('вы ',zodiac[11])
# else:
#     print('ахахах шутник!')


# lesson_04
# перебор массива и выдача четных символов

# nums = list(range(1, 100))
# nums2 = ''
#
# for nums2 in nums:
#     if nums2 % 7 == 0:
#         print(nums2)


# x = 'это предложение будет выведенно лесенкой'
# z = ''
# for i, s in enumerate(x):
#     if i % 2 == 0:
#         z += s.upper()
#     else:
#         z += s
# print(z)


# mans = []
# womans = []
#
# i = 0
# while i <= 5:
#     qs1 = input('как вас зовут?')
#     qs2 = input('какой у вас пол?')
#     if qs2 == 'man':
#         mans.append(qs1)
#         print(mans)
#     elif qs2 == 'woman':
#         womans.append(qs1)
#         print(womans)
#     else:
#         print('что то пошло не так')
#     i += 1

# vse = ['kartoshka', 'smorodina', 'yabloki', 'grushi','morkovka', 'luk', 'pomidor', 'apelsini','arbuz']
# ovoshi = ['kartoshka', 'morkovka', 'luk', 'pomidor']
# frukti = ['yabloki', 'grushi', 'apelsini']
#
# for letter in vse:
#     if letter in ovoshi:
#         print(letter + ' это овощ')
#     elif letter in frukti:
#         print(letter + ' это фрукт')
#     else:
#         print(letter + 'это ягода')


# cars = list()
#
#
# def ques(i=1):
#     while i <= 3:
#         qs1 = input('введите марку автомобиля')
#         qs2 = input('введите модель автомобиля')
#         qs3 = input('введите год выпуска автомобиля')
#         a = {'brands': qs1, 'model': qs2, 'year': qs3}
#         cars.append(a)
#         i += 1
#         print(cars)
#
#
# ques()


# c = 0
#
# try:
#     a = int(input('введите сумму кредита'))
#     b = int(input('введите проценты по кредиту')).replace('%', '')
#     c = (a / 100) * b
# except ValueError:
#     print('вводите только числа')
# except ZeroDivisionError:
#     print("делить на ноль нельзя")
# except TypeError:
#     print('разные типы данных')
# except Exception:
#     print('что то пошло не так')
#
# print('ваш процент по выплате составляет: ', c, ' %')

# from mymath import other
# other.round()
# import mymath as m
# m.operations.arithmetic.add()
# import mymath.operations.trigonometric as trig
# trig.sin()
#
#
# class Worker:
#     salary = 0
#
#     def work(self, salary):
#         self.salary = salary
#         print(self.salary)
#
#     def __del__(self):
#         print('del')
#
#
# class Driver(Worker):
#
#     def __init__(self,  salary):
#         self.salary = salary
#         print(self.salary)
#
#     def work(self, salary):
#         print(self.salary)
#
#
# a = Worker()
# b = Driver()
#
# a.work()
# b.work()


# class SimpleIterator:
#     def __init__(self, limit=10):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration
#
#
# s_iter1 = SimpleIterator(10)
#
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))


# def simple_generator(val=10):
#     while val > 0:
#         val -= 1
#         yield val
#
#         yield val+23
#
# # Данная функция будет работать точно также, как класс SimpleIterator из предыдущего примера.
# gen_iter = simple_generator()
#
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))


# summa = (lambda x, y: x + y)(1, 2)
# some_list = list(range(1, 100, 7))
# q = list(map(lambda a: a ** 2, some_list))
# itr = iter(some_list)
#
# print(summa)
# print(q)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
