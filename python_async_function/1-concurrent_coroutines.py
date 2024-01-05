#!/usr/bin/env python3
"""wait for multiple routines and get their result in order of return
The wait_n function is an asynchronous Python function designed to simulate the
concurrent execution of multiple asynchronous tasks. The function takes two
parameters: n, an integer representing the number of tasks to execute
concurrently, and max_delay, an integer specifying the maximum delay each task
can incur. The function utilizes the asyncio module to manage the asynchronous
execution flow.

Within the function, a list named delays is initialized to store the delays
incurred by each asynchronous task. Subsequently, a list named tasks is
created, containing instances of the wait_random coroutine function. This
coroutine function presumably generates a random delay within the specified
max_delay.

The asyncio.as_completed function is then employed to iterate through the
completed tasks in the order they finish. For each completed task, the delay
value is obtained using the await keyword, and this delay is appended to the
delays list.

Finally, the function returns the list of delays, providing insight into the
duration of each asynchronous task. This function is suitable for scenarios
where parallel execution of asynchronous tasks with random delays is required,
offering a convenient way to retrieve and analyze the individual delays once
the tasks are completed.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    exec multiple routines at once
    The wait_n function is an asynchronous Python function designed to simulate
    the concurrent execution of multiple asynchronous tasks. The function takes
    two parameters: n, an integer representing the number of tasks to execute
    concurrently, and max_delay, an integer specifying the maximum delay each
    task can incur. The function utilizes the asyncio module to manage the
    asynchronous execution flow.

    Within the function, a list named delays is initialized to store the delays
    incurred by each asynchronous task. Subsequently, a list named tasks is
    created, containing instances of the wait_random coroutine function. This
    coroutine function presumably generates a random delay within the specified
    max_delay.

    The asyncio.as_completed function is then employed to iterate through the
    completed tasks in the order they finish. For each completed task, the
    delay value is obtained using the await keyword, and this delay is appended
    to the delays list.

    Finally, the function returns the list of delays, providing insight into
    the duration of each asynchronous task. This function is suitable for
    scenarios where parallel execution of asynchronous tasks with random delays
    is required, offering a convenient way to retrieve and analyze the
    individual delays once the tasks are completed.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays