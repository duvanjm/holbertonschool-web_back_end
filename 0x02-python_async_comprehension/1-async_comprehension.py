#!/usr/bin/env python3
"""module"""

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async
    comprehensing over async_generator"""
    lst = []
    async for i in async_generator():
        lst.append(i)
    return lst
