from generate_data import read_data_json

# TODO: Add another methods of picking items (by weight, by ratio, by penalties)
# Picking highest value items first
def greedy_knapsack(path_to_file):
    print("!!! Solving using greedy algorithm")

    data = read_data_json(path_to_file, True)

    current_value = 0
    current_weight = 0

    final_weights = {}
    final_values = {}

    while len(data["values"]):
        max_value = max(data["values"])
        max_value_index = data["values"].index(max_value)

        if (current_weight + data["weights"][(max_value_index)] > data["capacity"]):
            break
        else:
            last_used_value = data["values"].pop(max_value_index)
            last_used_weight = data["weights"].pop(max_value_index)
            last_used_cat_index = data["categories"].pop(max_value_index)

            final_weights[max_value_index] = last_used_weight
            final_values[max_value_index] = last_used_value

            # penalty_used = data["penalties"][][]
            current_value += last_used_value # * ((100 - penalty_used / 100)
            current_weight += last_used_weight

        print(f"Element used: weight = {last_used_weight}, value = {last_used_value}")

    print("!!! Solution found: ", f"Value: {current_value}", f"Weight: {current_weight}", sep="\n")
    print("!!! Elements used:", f"Values: {final_values}", f"Weights: {final_weights}", sep="\n")

def knapsack():
    pass