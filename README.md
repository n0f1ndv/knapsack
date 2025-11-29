# Binary Knapsack Problem with categories
## Instalation:
To get this repository please use:
    `git clone https://github.com/n0f1ndv/knapsack.git`

Right now current work is on dev:
    `git switch dev`
    
## Example usage:
This command generates data for  given problem and writes it in json format:
    `python3 src/main.py --generate-data json`
    
This command runs greedy algorithm to solve instance of problem:
    `python3 src/main.py --solve greedy data/example1.json`

This command runs genetic algorithm to solve instance of problem:
    `python3 src/main.py --solve genetic data/example1.json`