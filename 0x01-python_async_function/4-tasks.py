#!/usr/bin/env python3
"""module"""

from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    lst = []
    for i in range(n):
        lst.append(await task_wait_random(max_delay))
    return lst
