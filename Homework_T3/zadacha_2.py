name = (input("Введите ваше имя: "))
age = (input("Введите ваш возраст: "))
if age.isdigit() and name.isalpha():
    age = int(age)
    if int(age) <= 0:
        print("Ошибка, повторите ввод")
    elif int(age) > 0 and int(age) < 10:
        print(f"Привет, шкет {name}")
    elif int(age) >= 10 and int(age) <= 18:
        print(f"Как жизнь {name}?")
    elif int(age) > 18 and int(age) < 100:
        print(f"Что желаете {name}?")
    else:
        print(f"{name}, вы лжёте - в наше время столько не живут...")
else:
    print("Ошибка, повторите ввод")
