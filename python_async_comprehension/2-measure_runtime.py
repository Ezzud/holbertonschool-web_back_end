#!/usr/bin/env python3
"""Asynchronous coroutine"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns the time it takes to execute async_comprehension"""
    start = time.time()
    await asyncio.gather(async_comprehension())
    end = time.time()
    total = end - start
    return total
