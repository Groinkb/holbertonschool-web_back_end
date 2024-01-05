#!/usr/bin/env python3
"""turn two values into a key value tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """turn two values into a key value tuple"""
    return (k, v * v)