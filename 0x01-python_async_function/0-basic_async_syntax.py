#!/usr/bin/env python3
"""module"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
