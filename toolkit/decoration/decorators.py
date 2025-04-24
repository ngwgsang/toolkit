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

def cooldown(delay=3):
    """
    Delay for `delay` seconds after the decorated function completes.

    Args:
        delay: Number of seconds to wait after function execution.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"[cooldown] Cooling down for {delay} second(s)...")
            time.sleep(delay)
            return result
        return wrapper
    return decorator

def limit_calls(max_calls=5):
    def decorator(func):
        count = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= max_calls:
                raise RuntimeError(f"[limit_calls] {func.__name__} exceeded {max_calls} calls")
            count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_types(func):
    import inspect
    sig = inspect.signature(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            expected = sig.parameters[name].annotation
            if expected is not inspect._empty and not isinstance(value, expected):
                raise TypeError(f"[validate_types] {name} must be {expected}, got {type(value)}")
        return func(*args, **kwargs)
    return wrapper