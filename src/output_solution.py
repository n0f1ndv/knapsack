import json
from datetime import datetime

def output_solution(value, weight, penalty_value, final_value, elements_used):
    print("!!! Solution found: ", f"Value: {value}", f"Weight: {weight}", sep="\n")
    print("!!! Calculated penalty: ", f"Penalty: {penalty_value}", sep="\n")
    print("!!! Solution after subtracting penalty: ", f"Value: {final_value}", sep="\n")
    print("!!! Elements used:", f"{elements_used}", sep="\n")

def output_solution_json(value, weight, penalty_value, final_value, elements_used):
    file_name = f"data/sol_{datetime.today().strftime("%Y%m%d%H%M%S")}.json"
    print(f"!!! Saving solution in {file_name}")

    data = {}
    
    data["value"] = value
    data["weight"] = weight
    data["penalty_value"] = penalty_value
    data["final_value"] = final_value
    data["elements_used"] = elements_used

    with open(file_name, 'w') as file:
        json.dump(data, file)