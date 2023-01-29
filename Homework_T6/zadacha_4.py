import json
import csv
import random

with open("data_user_file.json", "r") as f:
    data = json.load(f)
    phones = (random.randrange(1000000))

    data_id = list(data.items())





with open("my.csv", "w") as file:
    writer = csv.writer(file)
    names = ['id', 'name', 'age', 'phone']
    writer.writerow(
        (names)
    )
    for i,i1 in data_id:
        writer.writerow(
                [i,i1[0],i1[1],phones]
        )

