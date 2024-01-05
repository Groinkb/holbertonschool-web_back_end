#!/usr/bin/env python3
"""measure runtime"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure time / n"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    delta = (time.time() - start) / n
    return delta