#!/usr/bin/env python3
"""Task 2: Measure Asynchronous Comprehension Runtime"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total time"""
    start = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end = time.time()
    total_time = end - start
    return total_time