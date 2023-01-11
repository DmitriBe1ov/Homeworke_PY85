import secrets
a = secrets.randbelow(5)
print("Попробуй угадать число от 0 до 5")
b = int(input("Введи сюда свое число-> "))
while a != b:
    a = secrets.randbelow(5)
    if b == a :
        print("Молодец, ты угадал число", a)
    else:
        print("Не угадал, я закадал число", a)
        b = int(input("Попробуй ещё раз-> "))
