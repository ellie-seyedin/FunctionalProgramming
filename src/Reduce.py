from functools import reduce 
import operator

# This is a function that takes two arguments. 
# The function is applied to the current cumulative result and the next item in the sequence.

numbers = [1, 2, 3, 356, 24, 45, 56, 64]
sum = reduce(lambda x, y : x + y , numbers)
print(sum)

multiply = reduce(lambda x, y : x * y, numbers)
print(multiply) 

concatenation = reduce(operator.concat, ['A', 'BB', 'C'])
print(concatenation)

