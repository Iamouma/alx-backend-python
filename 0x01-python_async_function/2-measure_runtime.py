#!/usr/bin/env python3

"""
A function with intergers n and max_delay as arguments that
measures the total execution time for wait_n and returns
total_time / n.
"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This returns total execution time
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time/n)
