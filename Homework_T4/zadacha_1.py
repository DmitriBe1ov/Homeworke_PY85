breakfast = {
    "tea": "tess",
    "coffee": "lavazza",
}
breakfast_new = {}


def invert(dct):
    breakfast_new.update({dct[i]: i for i in dct})
    return breakfast


invert(breakfast)
print(breakfast_new)
