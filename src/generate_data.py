import random
import json
from datetime import datetime

def generate_data(seed=None, user_provided=False):
    random.seed(seed)

    if (user_provided):
        print("Please provide minimum, maximum for following parameters:")
        min_num, max_num = list(map(int, input("items_number> ").split()))
        items_number = random.randint(min_num, max_num)

        min_val, max_val = list(map(int, input("values> ").split()))
        values = [random.uniform(min_val, max_val) for i in range(items_number)]
    
        min_wei, max_wei = list(map(int, input("weights> ").split()))
        weights = [random.uniform(min_wei, max_wei) for i in range(items_number)]

        min_cap, max_cap = list(map(int, input("capacity> ").split()))
        capacity = random.uniform(min_cap, max_cap)

        min_cat_num, max_cat_num = list(map(int, input("categories_number> ").split()))
        categories_number = random.randint(min_cat_num, max_cat_num)

        categories = [random.randint(0, categories_number - 1) for i in range(items_number)]

        min_pen, max_pen = list(map(int, input("penalties> ").split()))
        penalties = {}
        for i in range(categories_number):
            for j in range(i, categories_number):
                if (i == j):
                    continue
                else:
                    penalties[f"{i}{j}"] = random.randint(min_pen, max_pen)

    else:
        settings = read_data_json("src/settings/generator_settings.json")

        items_number = random.randint(*settings["items_number"])
        values = [random.uniform(*settings["values"]) for i in range(items_number)]
        weights = [random.uniform(*settings["weights"]) for i in range(items_number)]
        capacity = random.uniform(*settings["capacity"])

        categories_number = random.randint(*settings["categories_number"])
        categories = [random.randint(0, categories_number - 1) for i in range(items_number)]

        penalties = {}
        for i in range(categories_number):
            for j in range(i, categories_number):
                if (i == j):
                    continue
                else:
                    penalties[f"{i}{j}"] = random.randint(*settings["penalties"])

    return items_number, values, weights, capacity, categories_number, categories, penalties

def generate_data_json(file_name=None, seed=None, user_provided=False):
    raw_data = {}

    items_number, values, weights, capacity, categories_number, categories, penalties = generate_data(seed, user_provided)

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

    # Minizinc needs indices from 1..upper_bound so I am adding 1 to each category 
    categories = [i + 1 for i in categories]

    if file_name == None:
        file_name = f"{datetime.today().strftime("%Y%m%d%H%M%S")}_random_data"

    with open(f"data/{file_name}.dzn", 'w') as file:
        file.write(f"n = {items_number};\n")
        file.write(f"C = {capacity};\n")
        file.write(f"v = {values};\n")
        file.write(f"w = {weights};\n")
        file.write(f"c = {categories};\n")
        file.write(f"m = {categories_number};\n")

        file.write("l = [|")
        for i in range(0, categories_number):
            for j in range(0, categories_number):
                if i == j:
                    file.write("0,")
                elif (j > i):
                    file.write(f"{penalties[f"{i}{j}"]},")
                else:
                    file.write(f"{penalties[f"{j}{i}"]},")
            file.write("|")
        file.write("];\n")

def read_data_json(file_name, output_data=False):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

            # DEBUG
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