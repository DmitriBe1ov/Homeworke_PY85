from datetime import datetime
import time


def time_click(n):
    new_list = []
    for i in range(n):
        new_list.append([datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')])
        time.sleep(1)
    print(new_list)


time_click(int(input("Введите кол-во элементов нового списка: ")))
