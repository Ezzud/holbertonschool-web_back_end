#!/usr/bin/env python3
"""Write a coroutine called async_generator
with no argument"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    """Give random number between 0 and 10
    every 1 second, 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
