#!/usr/bin/env python3
"""wait some time"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """sleep between 0 and max"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay