#!/bin/bash

file_path="data/$2.json"

# ./src/knap.sh --gen example4 genetic
if [ "$1" == "--gen" ]; then
    echo "*** Generating file with data for instance of a problem" 
    python3 src/main.py --generate-data --from-settings json $2

    echo "*** Relative path to generated file: $file_path"

    echo "*** Running $3 algorithm to solve the problem"
    python3 src/main.py --solve $3 "$file_path"

elif [ "$1" == "--use" ]; then
    echo "*** Using file: $file_path"

    echo "*** Running $3 algorithm to solve the problem"
    python3 src/main.py --solve $3 "$file_path"  
fi