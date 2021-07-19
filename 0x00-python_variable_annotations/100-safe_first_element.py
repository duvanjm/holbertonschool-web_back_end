#!/usr/bin/env python3
"""module"""

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augment the code with the correct
    duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
