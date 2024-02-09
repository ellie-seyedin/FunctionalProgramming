# map(function, iterable): Applies a function to all the items in an input list.
#built-in functions often used with iterators.

# map example
numbers = [1,2,3,4]
squared = map(lambda x : x ** 2, numbers)
print(list(squared))


def upper(s):
    return s.upper()

words = ['sentence', 'fragment']
upper_case = list(map(upper, words))
print(upper_case)
