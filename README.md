# Binary Knapsack Problem with categories
## Instalation:
To get this repository please use:
    `git clone https://github.com/n0f1ndv/knapsack.git`

Right now current work is on dev:
    `git switch dev`
    
## Example usage:
This command generates data for given problem and writes it in json format:
    When prompted about file name DO NOT enter extension. Only file name, you may leave name empty and then 
    program will choose name after current date.
    To generate a file you only need to provide the name, without extension. It is saved in data directory.
    `python3 src/main.py --generate-data json example1`
    
This command runs greedy algorithm to solve instance of problem:
    `python3 src/main.py --solve greedy data/example1.json`

This command runs genetic algorithm to solve instance of problem:
    `python3 src/main.py --solve genetic data/example1.json`
As you can see you need to provide relative path to file with data to solve it.

This command generates data for brute force algorithm in minizinc and runs the solver for generated data:
    Make this script executable:
    `chmod +x src/minizinc/brute.sh`
    Generate data using python script with dzn parameter:
    `python src/main.py --generate-data dzn`
    Run this script with path to chosen data file:
    `./src/minizinc/brute.sh data/example0.dzn`

How to use knap.sh:
    Make this script executable:
    `chmod +x src/knap.sh`
    To generate new data and solve it using algorithm:
    `./src/knap.sh --gen example5 greedy`
    To use already existing data and solve it use:
    `./src/knap.sh --use example5 genetic`
    Notice that you only need to provide name of file from data directory.