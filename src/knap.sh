#!/bin/bash

if [ "$3" == "genetic" ] || [ "$3" == "greedy" ]; then
    file_path="data/$2.json"

    if [ "$1" == "--gen" ]; then
        echo "*** Generating file with data for instance of a problem" 
        python3 src/main.py --generate-data --from-settings json $2
 
        echo "*** Relative path to generated file: $file_path"
 
        echo "*** Running $3 algorithm to solve the problem"
        python3 src/main.py --solve $3 $4 "$file_path"
 
    elif [ "$1" == "--use" ]; then
        echo "*** Using file: $file_path"
 
        echo "*** Running $3 algorithm to solve the problem"
        python3 src/main.py --solve $3 $4 "$file_path"  
    fi
elif [ "$3" == "brute" ]; then
    file_path="data/$2.dzn"
 
    if [ "$1" == "--gen" ]; then
        echo "*** Generating file with data for instance of a problem" 
        python3 src/main.py --generate-data --from-settings dzn $2
 
        echo "*** Relative path to generated file: $file_path"
 
        echo "*** Running $3 algorithm to solve the problem"
        exec timeout 60s minizinc src/minizinc/knapsack.mzn --json-stream --output-mode json "$file_path"
 
    elif [ "$1" == "--use" ]; then
        echo "*** Using file: $file_path"

        echo "*** Running $3 algorithm to solve the problem"
        exec minizinc src/minizinc/knapsack.mzn --json-stream "$file_path"
    fi
else
    echo "Option was not recognized"
fi
