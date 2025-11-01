import random
import json
from datetime import datetime

"""
Example json genereted using this script
{
        "items_number": 4,
        "values": [1, 2, 3, 4],
        "weights": [4, 3, 2, 1],
        "capacity": 7,
        "categories": 2,
        # categories_loss indicates how n-1 and n category affect each other for n=categories (theres is n-1)
        "categories_effect": [0.9]
    }
"""
def generate_data(file_name=None, seed=None):
    random.seed(seed)

    raw_data = {}

    print("Please provide minimum, maximum for following parameters:")
    min_num, max_num = list(map(int, input("items_number> ").split()))
    items_number = random.randint(min_num, max_num)
    raw_data["items_number"] = items_number

    min_val, max_val = list(map(int, input("values> ").split()))
    raw_data["values"] = [random.randint(min_val, max_val) for i in range(items_number)]

    min_wei, max_wei = list(map(int, input("weights> ").split()))
    raw_data["weights"] = [random.randint(min_wei, max_wei) for i in range(items_number)]

    min_cap, max_cap = list(map(int, input("capacity> ").split()))
    raw_data["capacity"] = random.randint(min_cap, max_cap)

    min_cat, max_cat = list(map(int, input("categories> ").split()))
    raw_data["categories"] = random.randint(min_cat, max_cat)

    raw_data["categories_effect"] = random.random()

    if file_name == None:
        file_name = f"{datetime.today().strftime("%Y%m%d%H%M%S")}_random_data.json"

    with open(file_name, 'w') as file:
        json.dump(raw_data, file)

def read_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)

    except FileNotFoundError:
        print("ERROR: File was not found")
        