#!/usr/bin/env python3
"""
Importing the asyncio module and the
random module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    named wait_random that waits for a random delay between
    0 and max_delay seconds and eventually returns it.
    """

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
