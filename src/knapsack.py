from time import sleep

from generate_data import read_data_json

# Sorting array by sorting it in ratio of value to weight
def greedy_knapsack(path_to_file):
    data = read_data_json(path_to_file, True)

    current_value = 0
    current_weight = 0

    while len(data["values"]):
        max_value = max(data["values"])
        max_value_index = data["values"].index(max_value)

        if (current_weight + data["weights"][(max_value_index)] > data["capacity"]):
            break
        else:
            value_used = data["values"].pop(max_value_index)
            weight_used = data["weights"].pop(max_value_index)
            current_value += value_used
            current_weight += weight_used

        print(f"Element used: weight = {weight_used}, value = {value_used}")

    print("Solution found: ", f"Value: {current_value}", f"Weight: {current_weight}", sep="\n")

def knapsack():
    pass