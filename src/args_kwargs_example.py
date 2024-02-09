
# *args and **kwargs are powerful features in Python that allow you to write flexible functions
# that can accept a varying number of arguments. 
# They are commonly used in cases where the number of arguments is not known in advance 
# or when you want to delegate argument handling to another function

def my_function(*args):
    for arg in args:
        print(arg)

numbers = [1, 2, 3, 356, 24, 45, 56, 64]

my_function(numbers)


# **kwargs allows you to pass a variable number of keyword arguments to a function. When a function parameter is prefixed with two asterisks (**), 
#it collects all the keyword arguments into a dictionary where the keys are the argument n ames and the values are the argument values.

def my_function(**kwargs):
    results = []
    for key, value in kwargs.items():
        results.append(f"{key}: {value}")
    return results

fun = my_function(name='Alice', age=30, city='New York')
print(fun)

# Using *args and **kwargs Together
# *args must appear before **kwargs

def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(1, 2, 3, name='Alice', age=30)


#When calling a function that uses *args and/or **kwargs, you can pass any number of positional or keyword arguments.

def example_function(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"Additional positional arguments (*args): {args}")
    print(f"Additional keyword arguments (**kwargs): {kwargs}")

example_function(1, 2, 3, 4, 5, name='Alice', age=30)