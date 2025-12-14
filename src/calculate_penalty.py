def calculate_penalty(data, used_elements_indices):
    penalty_value = 0

    for i in range(len(used_elements_indices) - 1):
        current_pos = used_elements_indices[i]
        next_pos = used_elements_indices[i+1]

        if (data["categories"][current_pos] == data["categories"][next_pos]):
            continue

        if (data["categories"][next_pos] > data["categories"][current_pos]):
            key = f"{data["categories"][current_pos]}{data["categories"][next_pos]}"
        else:
            key = f"{data["categories"][next_pos]}{data["categories"][current_pos]}"
        
        penalty_value += (data["penalties"][key] / 100) * (data["values"][current_pos] + data["values"][next_pos])

    return penalty_value
