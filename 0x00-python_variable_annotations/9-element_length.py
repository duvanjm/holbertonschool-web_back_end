#!/usr/bin/env python3
"""module"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Augment the code with the correct duck-typed annotations:"""
    return [(i, len(i)) for i in lst]
