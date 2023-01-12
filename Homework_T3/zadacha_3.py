name = (input("Введите ваше имя: "))
age = (input("Введите ваш возраст: "))
while 2 == 2:
    if age.isdigit() and name.isalpha():
        age = int(age)
        if age <= 0:
            print("Ошибка, повторите ввод")
            name = (input("Введите ваше имя ещё раз: "))
            age = (input("Введите ваш возраст ещё раз: "))
        elif age > 0 and age < 10:
            print(f"Привет, шкет {name}")
            name = (input("Введите ваше имя ещё раз: "))
            age = (input("Введите ваш возраст ещё раз: "))
        elif age >= 10 and age <= 18:
            print(f"Как жизнь {name}?")
            name = (input("Введите ваше имя ещё раз: "))
            age = (input("Введите ваш возраст ещё раз: "))
        elif age > 18 and age < 100:
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
