import sys

from generate_data import *

def main():
    if len(sys.argv) == 1:
        print(
            "Usage: python3 src/main.py <option>",
            "Available options:",
            "--generate-data - generates random input data based on specified "
            "min and max value given by user then saves it in a json file",
            sep='\n'
            )
    else:
        pass

    if sys.argv[1] == "--generate-data":
        tmp = input("file name> ")
        file_name = tmp if len(tmp) else None

        tmp = input("seed> ")
        seed = int(tmp) if len(tmp) else None
        print(seed)

        generate_data(file_name, seed)

if __name__ == "__main__":
    main()