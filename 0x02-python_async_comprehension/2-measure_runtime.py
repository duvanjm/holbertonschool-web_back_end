#!/usr/bin/env python3
"""module"""

import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times"""
    for i in range(4):
        t1 = time.time()
        await asyncio.gather(async_comprehension())
        t2 = time.time()
    return t2 - t1
