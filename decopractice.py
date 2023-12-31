# #Two different decorators, function and class decorators
# import functools
# #Like java annotation driven springboot.
#
# def start_end_decorator(func):
#
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("start")
#         result = func(*args, **kwargs)
#         print("end")
#         return result
#     return wrapper
#
# @start_end_decorator
# def print_name():
#     print('salmon')
#
# # print_name() #Now the behavior has been extended.
# @start_end_decorator
# def add5(x):
#     return x + 5
# # result = add5(10)
# # print(result)
# # print(help(add5))
# # print(add5.__name__)
#
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         #Do something inside
#         result = "hello"
#         result += " " + str(*args, **kwargs)
#         print(result)
#         return result
#     return wrapper
#
# @my_decorator
# def say_hi(name):
#     return print(name)
#
# # say_hi('salmon')
#
# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat
#
# @repeat(num_times=3)
# def greet(name):
#     print(f'Hello {name}')
#
# # greet('salmon')
#
#
# #Nested decorators
#
# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper
#
# @debug
# @start_end_decorator
# def say_hello(name):
#     greeting = f'Hello {name}'
#     print(greeting)
#     return greeting
#
# # say_hello('salmon')
#

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This has been executed {self.num_calls} times')
        return self.func(*args, **kwargs)



@CountCalls
def say_hello():
    print("Hello")
# say_hello()
# say_hello()