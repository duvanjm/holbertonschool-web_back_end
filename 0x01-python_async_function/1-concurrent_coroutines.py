#!/usr/bin/env python3
"""module"""

from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    lst = []
    for i in range(n):
        lst.append(await wait_random(max_delay))
    return sorted(lst)
