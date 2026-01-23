import sys
import csv
import json
import time
import matplotlib.pyplot as plt
from datetime import datetime

from genetic_knapsack import genetic_knapsack
from generate_data import read_data_json

TEST_DATA_PATH = "data/example8.json"
SETTINGS_PATH = "src/settings/genetic_settings.json"

def plot(path_to_csv_file):
    x = []
    y = []

    with open(path_to_csv_file, "r", newline="") as csv_file:
        lines = csv.reader(csv_file, delimiter=",")
        for line in lines:
            x.append(line[0])
            y.append(line[1])

    plt.plot(x, y, color = "r", linestyle = "dashed",
        marker = "o",label = "Time test")

    plt.xticks(rotation = 25)
    plt.xlabel("Time")
    plt.ylabel("Solution")
    plt.title("Time test", fontsize = 20)
    plt.grid()
    plt.legend()
    plt.show()

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
            settings["generations"] = gen
    
            start = time.time()
            solution = genetic_knapsack(data, settings, minimize=True)
            end = time.time()
    
            time_elapsed = round(1000 * (end - start), 3)
    
            results.append([time_elapsed, solution[3]])
    
        with open(f"test_results/time_test{datetime.today().strftime("%Y%m%d%H%M%S")}.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(results)

    elif sys.argv[1] == "--plot":
        plot(sys.argv[2])

if __name__ == "__main__":
    main()
