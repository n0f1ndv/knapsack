import random
import json
from datetime import datetime

# IMPORTANT: TESTING IN PROGRESS

# TODO:
# * Add doxygen style documentation
# * Change random.randint() to better random generator
def generate_data(seed=None):
    random.seed(seed)

    print("Please provide minimum, maximum for following parameters:")
    min_num, max_num = list(map(int, input("items_number> ").split()))
    items_number = random.randint(min_num, max_num)

    min_val, max_val = list(map(int, input("values> ").split()))
    values = [random.randint(min_val, max_val) for i in range(items_number)]

    min_wei, max_wei = list(map(int, input("weights> ").split()))
    weights = [random.randint(min_wei, max_wei) for i in range(items_number)]

    min_cap, max_cap = list(map(int, input("capacity> ").split()))
    capacity = random.randint(min_cap, max_cap)

    min_cat_num, max_cat_num = list(map(int, input("categories_number> ").split()))
    categories_number = random.randint(min_cat_num, max_cat_num)

    categories = [random.randint(0, categories_number - 1) for i in range(items_number)]

    min_pen, max_pen = list(map(int, input("penalties> ").split()))
    penalties = {}
    for i in range(categories_number):
        for j in range(i, categories_number):
            penalties[f"{i}{j}"] = random.randint(min_pen, max_pen)

    return items_number, values, weights, capacity, categories_number, categories, penalties

def generate_data_json(file_name=None, seed=None):
    raw_data = {}

    items_number, values, weights, capacity, categories_number, categories, penalties = generate_data(seed)

    raw_data["items_number"] = items_number
    raw_data["values"] = values
    raw_data["weights"] = weights
    raw_data["capacity"] = capacity
    raw_data["categories_number"] = categories_number
    raw_data["categories"] = categories
    raw_data["penalties"] = penalties

    if file_name == None:
        file_name = f"{datetime.today().strftime("%Y%m%d%H%M%S")}_random_data"

    with open(f"data/{file_name}.json", 'w') as file:
        json.dump(raw_data, file)

def generate_data_dzn(file_name=None, seed=None):
    items_number, values, weights, capacity, categories_number, categories, penalties = generate_data(seed)

    if file_name == None:
        file_name = f"{datetime.today().strftime("%Y%m%d%H%M%S")}_random_data"

    with open(f"src/minizinc/{file_name}.dzn", 'w') as file:
        file.write(f"n = {items_number};\n")
        file.write(f"capacity = {capacity};\n")
        file.write(f"values = {values};\n")
        file.write(f"weights = {weights};\n")
        file.write(f"categories = {categories};\n")
        file.write(f"m = {categories_number};\n")

        file.write("penalties = [|")
        for i in range(0, categories_number):
            for j in range(0, categories_number):
                file.write(f"{penalties[i][j]},")
            file.write("|")
        file.write("];\n")

def read_data_json(file_name, output_data=False):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

            if (output_data):
                print(5*"=", f"Data provided from {file_name}", 5*"=")
                print(f"n = {data["items_number"]}")
                print(f"capacity = {data["capacity"]}")
                print(f"values = {data["values"]}")
                print(f"weights = {data["weights"]}")
                print(f"categories = {data["categories"]}")
                print(f"m = {data["categories_number"]}")
                print(f"penalties = {data["penalties"]}")
                print(50*"=")

            return data

    except FileNotFoundError:
        print("ERROR: File was not found")