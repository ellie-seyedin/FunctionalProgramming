"""A decorator is simply a function which takes a function as a parameter and returns a function.

decorators are a very powerful and useful tool that allows you to modify the behavior of a function or a class method without
 permanently modifying it. Decorators wrap a function, allowing you to execute code before and after the wrapped function runs,
 without changing the function itself."""


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


""" The functools module provides a few decorators, such as lru_cache which can do what we just did: memoization.
functools.lru_cache can be used to optimize function calls by caching the results of previous calls and reusing them when the same inputs occur again"""

from functools import lru_cache

@lru_cache(maxsize=None)  # None means no limit on the cache size
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate factorial with memoization
print(factorial(5))  # This will calculate factorial(5) and cache its result
print(factorial(10))  # This will reuse the cached result of factorial(5) to calculate factorial(10)


