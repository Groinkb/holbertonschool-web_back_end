#!/usr/bin/env python3
"""annote this function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function annotated"""
    return [(i, len(i)) for i in lst]