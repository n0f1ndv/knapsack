#!/bin/bash

echo "*** Generating file with data for instance of a problem" 
python3 src/main.py --generate-data --from-settings json $2
echo "*** Running algorithm to solve the problem"
python3 src/main.py --solve $1 data/$2.json