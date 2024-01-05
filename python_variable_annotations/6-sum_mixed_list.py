#!/usr/bin/env python3
"""sums a list of mixed values"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums a list of mixed values"""
    return sum(mxd_lst)