#!/usr/bin/env python3
"""Write a coroutine called async_generator
with no argument"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """The coroutine will loop 10 times, wait
    10 seconds, and give a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
