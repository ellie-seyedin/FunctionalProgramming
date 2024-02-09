L = [1, 2, 3]
it = iter(L)

for i in it:
    print(i)  

# it.__next__()  # same as next(it)

# next(it)
 
 #Iterators can be materialized as lists or tuples by using the list() or tuple() constructor functions:
li = [10, 2, 3]
iterator = iter(li)
t = tuple(iterator)
print(t)

# Data Types That Support Iterators¶
month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
     'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
for key in month:
    print(key, month[key])

# Applying iter() to a dictionary always loops over the keys, but dictionaries have methods that return other iterators.
# If you want to iterate over values or key/value pairs, 
# you can explicitly call the values() or items() methods to get an appropriate iterator




# The dict() constructor can accept an iterator that returns a finite stream of (key, value) tuples:

L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
print(dict(iter(L)))



"""itertools is a module in the standard library that allows you to create iterators for efficient looping.

For example, permutations allows you to generate all the possible ways of ordering a set of things"""

from itertools import permutations

for p in permutations([1,2,3]):
    print(p)


"""Similarly, combinations generates all the possible ways of selecting items from a collection, 
such that (unlike permutations) the order does not matter:"""

from itertools import combinations

for c in combinations([1, 2, 3, 4], 2):
    print(c)


"""itertools also contains utility functions such as chain, 
which takes iterables and creates a new iterator that returns elements from the given iterables sequentially, as a single sequence:
"""
from itertools import chain

for c in chain(range(2), range(12, 15)):
    print(c)
