a = (input("Введите число: "))


def filter_1(a):
    b = a.replace("-", "")
    b = a.replace(".", "")

    if not b.isdigit():
        print("Вы ввели некоректное значение")
    elif a.startswith("-") and a.count(".") == 0:
        a = int(a)
        print(f"Вы ввели отрицательное целое число: {a}")
    elif a.startswith("-") and a.count(".") == 1:
        a = float(a)
        print(f"Вы ввели отрицательное дробное число: {a}")
    elif not a.startswith("-") and a.count(".") == 0:
        a = int(a)
        print(f"Вы ввели положительное целое число: {a}")
    elif not a.startswith("-") and a.count(".") == 1:
        a = float(a)
        print(f"Вы ввели положительное дробное число: {a}")

    else:
        print("ddd")


filter_1(a)
