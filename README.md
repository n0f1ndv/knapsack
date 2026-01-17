# Binary Knapsack Problem with categories
## Instalation:
To get this repository please use:
    `git clone https://github.com/n0f1ndv/knapsack.git`

Right now current work is on dev:
    `git switch dev`

Make this script executable:
    `chmod +x src/knap.sh`
    
## Example usage:
This command generates data for given problem and writes it in json format:
    When prompted about file name DO NOT enter extension. Only file name, you may leave name empty and then 
    program will choose name after current date.
    To generate a file you only need to provide the name, without extension. It is saved in data directory.
    Last parameter is seed, if you don't need to provide it.
    `python3 src/main.py --generate-data --from-settings json example1 123`

    `python src/main.py --generate-data --from-settings dzn example2 123`

This command runs brute force algorithm  in Minizinc to solve instance of problem:
    `./src/knap.sh --use example2 brute`

This command runs greedy algorithm to solve instance of problem without rearraging:
    `python3 src/main.py --solve greedy --dont-minimize data/example1.json`

This command runs genetic algorithm to solve instance of problem with rearranging elements in backpack after finding solution:
    `python3 src/main.py --solve genetic --minimize data/example1.json`
As you can see you need to provide relative path to file with data to solve it.

How to use knap.sh:
To generate new data and solve it using algorithm:
    `./src/knap.sh --gen example5 greedy --minimize`
    
To use already existing data and solve it use:
    `./src/knap.sh --use example5 genetic --dont-minimize`

To run test for algorithm use:
    `./src/knap.sh --test 20 greedy --minimize`
This will run greedy algorithm with --minimize option 20 times for generated data 
    
Notice that to generate you only need to provide name of file from 'data' directory.