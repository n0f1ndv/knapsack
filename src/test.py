"""
@file test.py
@brief Provides time test, quality test and RAM test also provides output of csv data as a lsit to the standard output
"""

import sys
import csv
import json
import time
import os
from datetime import datetime

from genetic_knapsack import genetic_knapsack
from greedy_knapsack import greedy_knapsack
from generate_data import *
from measure_memory import measure_memory

# SEED = 12349587
SEED = 94057234
TEST_DATA_PATH = "data/example10.json"
SETTINGS_PATH = "src/settings/genetic_settings.json"

def plot(path_to_csv_file):
    x = []
    y = []

    with open(path_to_csv_file, "r", newline="") as csv_file:
        lines = csv.reader(csv_file, delimiter=",")
        for i, line in enumerate(lines):
            if i > 0:
                x.append(float(line[0]))
                y.append(float(line[1]))

    print(x)
    print(y)

def main():
    if len(sys.argv) == 1:
        print("To learn how to use this program read README.md ;)")
        sys.exit(0)

    if sys.argv[1] == "--time-test":
        data = read_data_json(TEST_DATA_PATH)
        settings = read_data_json(SETTINGS_PATH)

        generations_number = range(int(input("start> ")), int(input("end> ")), int(input("step> ")))
    
        results = []
        results.append(["time", "solution"])
    
        for gen in generations_number:
            print(f"Test in progress {gen}")
            settings["generations"] = gen
    
            start = time.time()
            solution = genetic_knapsack(data, settings, minimize=True)
            end = time.time()
    
            time_elapsed = round(1000 * (end - start), 3)
    
            results.append([time_elapsed, solution[3]])
    
        with open(f"test_results/time_test{datetime.today().strftime("%Y%m%d%H%M%S")}.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(results)

    elif sys.argv[1] == "--quality-test":
        generator_settings = read_data_json("src/settings/generator_settings.json")

        results = []
        results.append(["greedy", "genetic"])

        for i in range(2, 9):
            print(f"Test in progress {i}")
            generator_settings["items_number"] = [2**i, 2**i]

            to_json = json.dumps(generator_settings)
            with open("src/settings/generator_settings.json", "w") as json_file:
                json_file.write(to_json)

            generate_data_dzn(f"test/test_{2**i}", SEED)
            generate_data_json(f"test/test_{2**i}", SEED)

            solution_greedy = greedy_knapsack(read_data_json(f"data/test/test_{2**i}.json"), minimize=False)
            solution_genetic = genetic_knapsack(read_data_json(f"data/test/test_{2**i}.json"), read_data_json(SETTINGS_PATH), minimize=False)

            results.append([solution_greedy[3], solution_genetic[3]])
            print(solution_genetic[1])

        with open(f"test_results/quality_test{datetime.today().strftime("%Y%m%d%H%M%S")}.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(results)

    elif sys.argv[1] == "--mem-test":
        generator_settings = read_data_json("src/settings/generator_settings.json")

        results = []
        results.append(["greedy", "genetic"])

        for i in range(2, 11):
            print(f"Test in progress {i}")
            generator_settings["items_number"] = [2**i, 2**i]

            to_json = json.dumps(generator_settings)
            with open("src/settings/generator_settings.json", "w") as json_file:
                json_file.write(to_json)

            generate_data_dzn(f"test/test_{2**i}", SEED)
            generate_data_json(f"test/test_{2**i}", SEED)

            mem_used_genetic = measure_memory(genetic_knapsack, (read_data_json(f"data/test/test_{2**i}.json"), read_data_json(SETTINGS_PATH), False))
            mem_used_greedy = measure_memory(greedy_knapsack, (read_data_json(f"data/test/test_{2**i}.json"), False))

            results.append([mem_used_greedy, mem_used_genetic])

        with open(f"test_results/mem_test{datetime.today().strftime("%Y%m%d%H%M%S")}.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(results)

    elif sys.argv[1] == "--plot":
        plot(sys.argv[2])

if __name__ == "__main__":
    main()
