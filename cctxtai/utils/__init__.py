from cctxtai.utils.logging import create_logger

UTIL_LOG = create_logger("utils", "DEBUG")


def timer(func):
    """
    Print the runtime of the decorated function
    """
    import functools
    import time

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        UTIL_LOG.info(f"Finished {func.__name__!r} in {run_time:.6f} secs")
        return value

    return wrapper_timer
