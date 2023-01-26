import json
user_data = {"000001": ("Andrey", 20),
             "000002": ("Aleksandr", 21),
             "000003": ("Ivan", 22),
             "000004": ("Oleg", 23),
             "000005": ("Evgeniy", 24),
             "000006": ("Maksim", 25)}

with open("data_user_file.json", "w") as file:
    json.dump(user_data, file, indent=4)
