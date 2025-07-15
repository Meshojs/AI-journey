# import time

# class Tools: 
#     @staticmethod
#     def fnTimer(fn): 
#         def wrapper(*args, **kwargs): 
#             start = time.time()
#             result = fn(*args, **kwargs)
#             end = time.time()
#             print(f"Function Spent : {round(end - start, 3)}s")
#             return result
#         return wrapper

#     @staticmethod
#     def Logger(fn):
#         def wrapper(*args, **kwargs): 
#             print("Running:", fn.__name__,"()")
#             result = fn(*args, **kwargs)
#             print("Function returned:", result)
#             return result
#         return wrapper
def greet(name):
    print("hello ", name)