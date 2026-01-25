"""
@file greedy_knapsack.py
@brief Provides greedy algorithm for an instance of a problem
"""

from generate_data import read_data_json
from calculate_penalty import calculate_penalty
from minimize_penalty import minimize_penalty

def greedy_knapsack(data, minimize=False):
    """
    @brief Greedy algorithm that picks items by highest value
    @param data (dict): Instance of a problem read from json
    @param minimize (bool): Decides whether to call minimize_penalty()
    """
    total_value = 0
    total_weight = 0
    elements_used = [0] * data["items_number"]
    used_elements_indices = []

    values, weights, indices = zip(*sorted(zip(
        data["values"],
        data["weights"],
        range(data["items_number"])), reverse=True)
    )

    for value, weight, index in zip(values, weights, indices):
        total_value += value
        total_weight += weight
        elements_used[index] = 1
        used_elements_indices.append(index)

        if (total_weight > data["capacity"]):
            total_weight -= weight
            total_value -= value
            elements_used[index] = 0
            used_elements_indices.remove(index)
            break
        
    if (minimize):
        used_elements_indices = minimize_penalty(data, used_elements_indices)

    total_penalty = calculate_penalty(data, used_elements_indices)

    return total_value, total_weight, total_penalty, total_value - total_penalty, elements_used
