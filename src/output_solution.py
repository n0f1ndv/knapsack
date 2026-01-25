"""
@file output_solution.py
@brief Module that provides outputting solution into terminal or json file
"""

import json
from datetime import datetime

def output_solution(value, weight, penalty_value, final_value, elements_used):
    """
    @brief Outputs solution to standard output
    @param data (dict): Data of an instance
    @param used_elements_indices (list): Contains a proper order of elements in knapsack
    """
    print("!!! Solution found: ", f"Value: {value}", f"Weight: {weight}", sep="\n")
    print("!!! Calculated penalty: ", f"Penalty: {penalty_value}", sep="\n")
    print("!!! Solution after subtracting penalty: ", f"Value: {final_value}", sep="\n")
    print("!!! Elements used:", f"{elements_used}", sep="\n")

def output_solution_json(value, weight, penalty_value, final_value, elements_used, time_elapsed, file_name=None):
    """
    @brief Outputs solution to json file
    @param value (float):
    @param weight (float):
    @param penalty_value (float):
    @param final_value (float):
    @param elements_used (list):
    @param time_elapsed (float):
    @param file_name (string)
    """
    if file_name is None:
        file_name = f"solutions/sol_{datetime.today().strftime("%Y%m%d%H%M%S")}.json"
    else: 
        file_name = f"solutions/{file_name}.json"

    print(f"!!! Saving solution in {file_name}")

    data = {}
    
    data["value"] = value
    data["weight"] = weight
    data["penalty_value"] = penalty_value
    data["final_value"] = final_value
    data["elements_used"] = elements_used
    data["time_elapsed"] = time_elapsed

    with open(file_name, 'w') as file:
        json.dump(data, file)
