from generate_data import read_data_json

# IMPORTANT: TESTING IN PROGRESS

# TODO: Add another methods of picking items (by weight, by ratio, by penalties)
# Picking highest value items first
def greedy_knapsack(data):
    current_value = 0
    current_weight = 0
    penalty_value = 0

    best_weights = []
    best_values = []
    best_categories = []

    while len(data["values"]):
        max_value = max(data["values"])
        max_value_index = data["values"].index(max_value)

        if (current_weight + data["weights"][(max_value_index)] > data["capacity"]):
            break
        else:
            best_weights.append(data["values"].pop(max_value_index))
            best_values.append(data["weights"].pop(max_value_index))
            best_categories.append(data["categories"].pop(max_value_index))

            current_value += best_values[-1]
            current_weight += best_weights[-1]

        # print(f"Element used: weight = {best_weights[-1]}, value = {best_values[-1]}, category = {best_categories[-1]}") # DEBUG

    for i in range(len(best_categories) - 1):
        if (best_categories[i+1] != best_categories[i]):
            if (best_categories[i+1] > best_categories[i]):
                penalty_value += (data["penalties"][f"{best_categories[i]}{best_categories[i+1]}"] / 100) * (best_values[i] + best_values[i+1])
            else:
                penalty_value += (data["penalties"][f"{best_categories[i+1]}{best_categories[i]}"] / 100) * (best_values[i] + best_values[i+1])

    final_value = current_value - penalty_value

    return current_value, current_weight, penalty_value, final_value, None
