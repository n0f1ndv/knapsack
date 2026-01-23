import sys
import time

from generate_data import *
from greedy_knapsack import *
from genetic_knapsack import *
from output_solution import *

def main():
    if len(sys.argv) == 1:
        print("To learn how to use this project read README.md ;)")
        sys.exit(0)

    if sys.argv[1] == "--generate-data":
        seed = None
        if (len(sys.argv) == 6):
            seed = sys.argv[5]

        if sys.argv[2] == "--user-provided":
            if sys.argv[3] == "dzn":
                generate_data_dzn(sys.argv[4], seed)
                
            elif sys.argv[3] == "json":
                generate_data_json(sys.argv[4], seed, True)

        elif sys.argv[2] == "--from-settings":
            if sys.argv[3] == "dzn":
                generate_data_dzn(sys.argv[4], seed)
                
            elif sys.argv[3] == "json":
                generate_data_json(sys.argv[4], seed)

        else:
            print("Option was not recognized.")
            exit(1)

    if sys.argv[1] == "--solve":
        if sys.argv[2] == "greedy":
            print("!!! Solving using greedy algorithm")

            if (sys.argv[3]) == "--minimize":
                minimize = True
            elif (sys.argv[3]) == "--dont-minimize":
                minimize = False

            start = time.time()
            solution = greedy_knapsack(read_data_json(sys.argv[4], True), minimize)
            end = time.time()

            time_elapsed = 1000000 * (end - start)
            print(f"### Execution time: {time_elapsed:.3f} ms")

            if (len(sys.argv) == 5):
                # output_solution(*solution)
                output_solution_json(*solution, time_elapsed)
            else:
                output_solution_json(*solution, time_elapsed, sys.argv[5])

        elif sys.argv[2] == "genetic":
            print("!!! Solving using genetic algorithm")

            if (sys.argv[3]) == "--minimize":
                minimize = True
            elif (sys.argv[3]) == "--dont-minimize":
                minimize = False

            start = time.time()
            solution = genetic_knapsack(read_data_json(sys.argv[4], True), read_data_json("src/settings/genetic_settings.json"), minimize)
            end = time.time()

            time_elapsed = 1000 * (end - start)
            print(f"### Execution time: {time_elapsed:.3f} s")

            # output_solution(*solution)
            output_solution_json(*solution, time_elapsed)

        else:
            print("Option was not recognized.")
            exit(1)

if __name__ == "__main__":
    main()
