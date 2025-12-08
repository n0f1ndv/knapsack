def output_solution(current_value, current_weight, penalty_value, final_value, elements_used):
    print("!!! Solution found: ", f"Value: {current_value}", f"Weight: {current_weight}", sep="\n")
    print("!!! Calculated penalty: ", f"Penalty: {penalty_value}", sep="\n")
    print("!!! Solution after subtracting penalty: ", f"Value: {final_value}", sep="\n")
    print("!!! Elements used:", f"{elements_used}", sep="\n")