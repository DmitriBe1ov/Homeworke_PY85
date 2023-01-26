print("Программа будет записывать введённые строки в файл\n")


def record_file():
    string_1 = input("Введите первую строку:")
    string_2 = input("Введиет вторую строку:")
    string_3 = input("Введите третью строку:")
    string_4 = input("Введите четвёртую строку:")
    with open("text.txt", "w") as file:
        file.write(string_1 + "\n")
        file.write(string_2 + "\n")
    with open("text.txt", "a") as file:
        file.write(string_3 + "\n")
        file.write(string_4 + "\n")


record_file()
