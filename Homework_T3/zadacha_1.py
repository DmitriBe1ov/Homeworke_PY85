text = (input("Введите предложение из двух слов: "))
text = text.split()
text = " ! ".join(text[::-1])
print(f"!{text}!")

text = (input("Введите предложение из двух слов: "))
text = text.split()
text = " ! ".join(text[::-1])
print("!{}!" .format(text))

text = (input("Введите предложение из двух слов: "))
text = text.split()
text = " ! ".join(text[::-1])
print("!%s!"%text)