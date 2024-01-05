#!/usr/bin/env python3
"""Task 1: Asynchronous Comprehension"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random"""
    random_numbers = [x async for x in async_generator()]
    return random_numbers