name = (input("Введите ваше имя: "))
age = (input("Введите ваш возраст: "))
while 2 == 2:
    if age.isdigit():
        if int(age) <= 0:
            print("Ошибка, повторите ввод")
            name = (input("Введите ваше имя ещё раз: "))
            age = (input("Введите ваш возраст ещё раз: "))
        elif int(age) > 0 and int(age) < 10:
            print(f"Привет, шкет {name}")
            name = (input("Введите ваше имя ещё раз: "))
            age = (input("Введите ваш возраст ещё раз: "))
        elif int(age) >= 10 and int(age) <= 18:
            print(f"Как жизнь {name}?")
            name = (input("Введите ваше имя ещё раз: "))
            age = (input("Введите ваш возраст ещё раз: "))
        elif int(age) > 18 and int(age) < 100:
            print(f"Что желаете {name}?")
            name = (input("Введите ваше имя ещё раз: "))
            age = (input("Введите ваш возраст ещё раз: "))
        else:
            print(f"{name}, вы лжёте - в наше время столько не живут...")
            name = (input("Введите ваше имя ещё раз: "))
            age = (input("Введите ваш возраст ещё раз: "))
    else:
        print("Ошибка, повторите ввод")
        name = (input("Введите ваше имя ещё раз: "))
        age = (input("Введите ваш возраст ещё раз: "))
