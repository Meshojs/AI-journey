import time

def teme(fn):
    def wrapper(*args, **kwargs):   # accept any args
        start = time.time()
        fn(*args, **kwargs)         # pass them on
        end = time.time()
        print(f"Function Spent about: {round(end - start, 2)}s")
    return wrapper
