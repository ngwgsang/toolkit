import time
import functools
import traceback

def retry(max_retries=3, delay=1, exceptions=(Exception,)):
    """
    Retry a function up to `max_retries` times with `delay` seconds between tries.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"[retry] Attempt {attempt}/{max_retries} failed: {e}")
                    if attempt == max_retries:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator


def trace(print_args=True, print_result=True):
    """
    Print function name, arguments, and return value — useful for debugging.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[trace] Calling: {func.__name__}")
            if print_args:
                print(f"[trace] Args: {args}, Kwargs: {kwargs}")
            try:
                result = func(*args, **kwargs)
                if print_result:
                    print(f"[trace] Result: {result}")
                return result
            except Exception as e:
                print(f"[trace] Error in {func.__name__}: {e}")
                traceback.print_exc()
                raise
        return wrapper
    return decorator

def timer(unit="s"):
    """
    Measure and print the execution time of the decorated function.
    
    Args:
        unit: 's' for seconds (default), 'ms' for milliseconds.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start
            if unit == "ms":
                print(f"[timer] {func.__name__} took {duration * 1000:.2f}ms")
            else:
                print(f"[timer] {func.__name__} took {duration:.2f}s")
            return result
        return wrapper
    return decorator