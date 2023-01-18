from datetime import datetime
import time


def time_click():
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


print([time_click() for i in range(int(input("Введите кол-во элементов нового списка: ")))])
