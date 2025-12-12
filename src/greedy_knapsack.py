from generate_data import read_data_json

# IMPORTANT: TESTING IN PROGRESS

# TODO: Add another methods of picking items (by weight, by ratio, by penalties)
# Picking highest value items first
def greedy_knapsack(data):
    final_value = 0
    final_weight = 0
    elements_used = [0] * data["items_number"]
    used_elements_indices = []
    penalty_value = 0

    values, weights, indices = zip(*sorted(zip(
        data["values"],
        data["weights"],
        range(data["items_number"])), reverse=True)
    )

    for value, weight, index in zip(values, weights, indices):
        final_value += value
        final_weight += weight
        elements_used[index] = 1
        used_elements_indices.append(index)

        if (final_weight > data["capacity"]):
            final_weight -= weight
            final_value -= value
            elements_used[index] = 0
            used_elements_indices.remove(index)
            break

    for i in range(len(used_elements_indices) - 1):
        current_pos = used_elements_indices[i]
        next_pos = used_elements_indices[i+1]

        if (data["categories"][current_pos] == data["categories"][next_pos]):
            continue

        if (next_pos > current_pos):
            key = f"{data["categories"][current_pos]}{data["categories"][next_pos]}"
        else:
            key = f"{data["categories"][current_pos]}{data["categories"][next_pos]}"
        
        print(data["values"][current_pos], data["values"][next_pos])
        penalty_value += (data["penalties"][key] / 100) * (data["values"][current_pos] + data["values"][next_pos])

    return final_value, final_weight, penalty_value, final_value - penalty_value, elements_used
