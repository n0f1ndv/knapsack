import sys

from generate_data import *
from knapsack import *

# TODO:
# * Add functions to solve instances of knapsack problem
#       (Do the research about available options)
# * Add error-handling
# * Add bash script that calls this program
def main():
    if len(sys.argv) == 1:
        print(
            "Usage: python3 src/main.py <option>",
            "Available options:",
            "--generate-data <file-type> - generates random input data based on specified",
            "min and max value given by user then saves it in a json file",
            "   available file types: dzn, json",
            "--solve <option> - ...",
            "   available options: greedy, ...",
            sep='\n'
            )
    else:
        pass

    if sys.argv[1] == "--generate-data":
        tmp = input("file name> ")
        file_name = tmp if len(tmp) else None

        tmp = input("seed> ")
        seed = int(tmp) if len(tmp) else None

        if sys.argv[2] == "dzn":
            generate_data_dzn(file_name, seed)
        elif sys.argv[2] == "json":
            generate_data_json(file_name, seed)
        else:
            print("Option was not recognized. Available options:")
            exit(1)

    if sys.argv[1] == "--solve":
        print("WORK IN PROGRESS (:_-_;)\n")
        if sys.argv[2] == "greedy":
            greedy_knapsack(sys.argv[3])
        elif sys.argv[2] == "":
            knapsack(sys.argv[3])
        else:
            print("Option was not recognized. Available options:")
            exit(1)

if __name__ == "__main__":
    main()