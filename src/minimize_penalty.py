"""
@file minimize_penalty.py
@brief Module providing funtion which may reduce penalty
"""

def minimize_penalty(data, used_elements_indices):
    """
    @brief Minimizes penalty by sorting categories so that the same categories are next to each other
    @param data (dict): Data of an instance
    @param used_elements_indices (list): Contains a proper order of elements in knapsack
    """
    used_categories = []

    for i in used_elements_indices:
        used_categories.append(data["categories"][i])

    used_categories, used_elements_indices = zip(*sorted(zip(used_categories, used_elements_indices)))
    
    return used_elements_indices
