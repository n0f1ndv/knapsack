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

    items_number = random.randint(min_num, max_num)
    values = [random.randint(min_val, max_val) for i in range(items_number)]
    weights = [random.randint(min_wei, max_wei) for i in range(items_number)]
    capacity = random.randint(min_cap, max_cap)
    categories = random.randint(min_cat, max_cat)
    categories_effect = random.random()