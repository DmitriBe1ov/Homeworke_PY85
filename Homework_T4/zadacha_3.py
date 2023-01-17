from collections import Counter

dct = {"номер": "123322343"}


def schetchik(your_dict):
    lst = []
    s = list(your_dict.values())
    for i in "".join(s):
        lst.append(i)
    a = Counter(lst)
    print(a)


schetchik(dct)
