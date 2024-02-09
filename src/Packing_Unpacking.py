"""The * operator, known as the unpack or splat operator allows very convenient transformations, 
going from lists or tuples to separate variables or arguments and conversely."""


#unpacking 
a, *b, c = [2, 7, 5, 6, 3, 4, 1]
print(a)
print(b)
print(c)


"""Packing in Python refers to the process of bundling multiple values into a single container, like a list or a tuple"""
def pack_args(*args):
    print(args)  # args is a tuple containing all passed positional arguments

pack_args(1, 2, 3, 'a', 'b')


# Packing into a Tuple
a = 1
b = 2
c = 3
packed_tuple = (a, b, c)  # Packing variables a, b, and c into a tuple
print(packed_tuple)

"""you can define a function that will pack all the arguments in a single tuple and all the keyword arguments in a single dict.
*args if it's a list
**kwargs if that's a dict.
"""
def f(*args, **kwargs):
    print("Arguments: ", args)
    print("Keyword arguments: ", kwargs)

f(3, 4, 9, foo=42, bar=7)