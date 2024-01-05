#!/usr/bin/env python3
"""create a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """create a function"""

    def f(n: float) -> float:
        """created function"""
        return n * multiplier

    return f