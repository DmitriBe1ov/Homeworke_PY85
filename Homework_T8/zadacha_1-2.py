import time


class Auto:
    def __init__(self, brand, age, mark, color="нет сведений", weight="нет сведений"):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        return "move"

    def stop(self):
        return "stop"

    def birthday(self):
        return self.age + 1


class Truck(Auto):
    def __init__(self, max_load):
        self.max_load = max_load

    def move(self):
        return "atantion " + super().move()

    def load(self):
        return f"{time.sleep(1)} load {time.sleep(1)}"


class Car(Auto):
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def move(self):
        return f"{super().move()} max speed is <{self.max_speed}>"


car = Auto("BMW", 12, "m5")
mercedes = Truck(100)
print(mercedes.move())
print(mercedes.load())
print(mercedes.max_load)
print(mercedes.stop())
mustang = Car(220)
print(mustang.max_speed)
print(mustang.move())
