#!/usr/bin/env python3
"""coroutine that execute asynchronously"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it"""
    start = time.time()
    await asyncio.gather(async_comprehension())
    end = time.time()
    total = end - start
    return total
