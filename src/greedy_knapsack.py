from generate_data import read_data_json

# IMPORTANT: TESTING IN PROGRESS

# TODO: Add another methods of picking items (by weight, by ratio, by penalties)
# Picking highest value items first
def greedy_knapsack(path_to_file):
    print("!!! Solving using greedy algorithm")

    data = read_data_json(path_to_file, True)

    current_value = 0
    current_weight = 0
    penalty_value = 0

    final_weights = []
    final_values = []
    final_categories = []

    while len(data["values"]):
        max_value = max(data["values"])
        max_value_index = data["values"].index(max_value)

        if (current_weight + data["weights"][(max_value_index)] > data["capacity"]):
            break
        else:
            final_weights.append(data["values"].pop(max_value_index))
            final_values.append(data["weights"].pop(max_value_index))
            final_categories.append(data["categories"].pop(max_value_index))

            current_value += final_values[-1]
            current_weight += final_weights[-1]

        print(f"Element used: weight = {final_weights[-1]}, value = {final_values[-1]}, category = {final_categories[-1]}")

    for i in range(len(final_categories) - 1):
        if (final_categories[i+1] > final_categories[i]):
            penalty_value += (data["penalties"][f"{final_categories[i]}{final_categories[i+1]}"] / 100) * (final_values[i] + final_values[i+1])
        else:
            penalty_value += (data["penalties"][f"{final_categories[i+1]}{final_categories[i]}"] / 100) * (final_values[i] + final_values[i+1])

    print("!!! Solution found: ", f"Value: {current_value}", f"Weight: {current_weight}", sep="\n")
    print("!!! Calculated penalty: ", f"Penalty: {penalty_value}")
    print("!!! Solution after subtracting penalty: ", f"Value: {current_value - penalty_value}", sep="\n")
    print("!!! Elements used:", f"Values: {final_values}", f"Weights: {final_weights}", f"Categories: {final_categories}", sep="\n")
