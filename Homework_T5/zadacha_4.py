from datetime import datetime


def dec(func):
    def wrapper():
        start = datetime.now()
        print(func())
        stop = datetime.now()
        print(f'Время выполнения {str(func).split()[1]} = {stop - start}')
        return func

    return wrapper()


@dec
def green():
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_list = list(map(lambda x: str(x), list_1))
    return new_list


@dec
def black():
    my_tuple = ("шалаш", "привет", "казак", "телефон")
    new_tuple = tuple(filter(lambda x: (x[::] == x[::-1]), my_tuple))
    return new_tuple


green()
black()
