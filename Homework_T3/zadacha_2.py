name = (input("Введите ваше имя: "))
age = (input("Введите ваш возраст: "))
if age != int or age <= 0 :
    print("Ошибка, повторите ввод")
elif age > 0 and age < 10:
    print(f"Привет, шкет {name}")
elif age >= 10 and age <= 18:
    print(f"Как жизнь {name}?")
elif age > 18 and age <100:
    print(f"Что желаете {name}?")
else:
    print(f"{name}, вы лжёте - в наше время столько не живут...")