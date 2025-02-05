import os
import time
from concurrent import futures
# from concurrent.futures import ThreadPoolExecutor

WORK_LIST = [10_000, 100_000, 1_000_000, 10_000_000]

def sum_generator(n):
    return sum(n for n in range(1, n + 1))

result = []

if __name__ == "__main__":
    print(os.cpu_count())
    worker = min(10, len(WORK_LIST))
    print(worker)
    start = time.time()

    with futures.ThreadPoolExecutor() as executor:
        result = executor.map(sum_generator, WORK_LIST)

    end = time.time()
    msg = "\n{} Time: {:.2f}s"

    print(msg.format(list(result), end - start))