# from datetime import datetime
#
# # Функции цикла и генератора  +++++++++++++++++++++++++++++++++++++++++++++++++
#
#
# def cycle():
#     temp = []
#     for x in range(1000):
#         if x % 2 == 0:
#             temp.append(x)
#
#
# def listing():
#     temp = [x for x in range(1000) if x % 2 == 0]
#
#
# # Функции цикла и генератора с декоратором  +++++++++++++++++++++++++++++++++++
#
#
# def decor(fun):
#     def wrapper():
#         start = datetime.now()
#         fun()
#         end = datetime.now()
#         print(f'Время выполнения {str(fun).split()[1]} = {end - start}')
#     return wrapper
#
#
# @decor
# def cycle():
#     temp = []
#     for x in range(10):
#         if x % 2 == 0:
#             temp.append(x)
#
#
# @decor
# def listing():
#     temp = [x for x in range(10) if x % 2 == 0]
#
#
# cycle()
# listing()
# def temp(x):
#     return x * temp(x - 1) if x != 1 else 1
#
#
# print(temp(5))
