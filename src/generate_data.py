import random
import json

from backend import *

"""
Example json genereted using this script
{
        "items_number": 4,
        "values": [1, 2, 3, 4],
        "weights": [4, 3, 2, 1],
        "capacity": 7,
        "categories": 2,
        # categories_loss indicates how n-1 and n category affect each other for n=categories (theres is n-1)
        "categories_effect": [0.9]
    }
"""
def generate_data(files_name=None, seed=None):
    random.seed(seed)

    print("Please provide minimum, maximum for following parameters:")
    print("\nitems_number> ")
    min_num, max_num = list(map(int, input().split()))
    items_number = random.randint(min_num, max_num)

    print("\nvalues> ")
    min_val, max_val = list(map(int, input().split()))
    values = [random.randint(min_val, max_val) for i in range(items_number)]

    print("\nweight> ")
    min_wei, max_wei = list(map(int, input().split()))
    weights = [random.randint(min_wei, max_wei) for i in range(items_number)]

    print("\ncapacity> ")
    min_cap, max_cap = list(map(int, input().split()))
    capacity = random.randint(min_cap, max_cap)

    print("\ncategories> ")
    min_cat, max_cat = list(map(int, input().split()))
    categories = random.randint(min_cat, max_cat)
    
    categories_effect = random.random()