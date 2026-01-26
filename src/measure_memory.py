"""
@file measure_memory.py
@brief Module that provides memory measure function
"""

import tracemalloc

def measure_memory(func, args):
    """
    @brief Helper function that calculates how much memory was used during function call.
    @param func: Function which memory usage is measured
    @param args (tuple): Arguments of func
    """
    tracemalloc.start()

    start_snapshot = tracemalloc.take_snapshot()

    func(*args)

    end_snapshot = tracemalloc.take_snapshot()

    stats = end_snapshot.compare_to(start_snapshot, "lineno")

    memory_used = sum(stat.size for stat in stats)
    tracemalloc.stop()

    return memory_used / (2 ** 10)
