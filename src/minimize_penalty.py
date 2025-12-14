def minimize_penalty(data, used_elements_indices):
    used_categories = []

    for i in used_elements_indices:
        used_categories.append(data["categories"][i])

    used_categories, used_elements_indices = zip(*sorted(zip(used_categories, used_elements_indices)))
    
    return used_elements_indices
