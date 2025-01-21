from typing import Callable, Any


def timer(block: Callable) -> Callable[[tuple[Any, ...], dict[str, Any]], Any]:
    def wrapper(*args, **kwargs):
        start = time.time()
        block(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Time taken: {duration} seconds")
        return duration
    return wrapper

@timer
def foo():
    time.sleep(1)

if __name__ == '__main__':
    import time
    foo()