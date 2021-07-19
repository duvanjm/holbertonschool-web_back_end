#!/usr/bin/env python3
"""module"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier"""

    def mul(n: float) -> float:
        """multiply a number"""
        return n * multiplier

    return mul
