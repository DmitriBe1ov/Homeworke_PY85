my_tuple = ("шалаш", "привет", "казак", "телефон")
new_tuple = tuple(filter(lambda x: (x[::] == x[::-1]), my_tuple))
print(new_tuple)
