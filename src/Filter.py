from functools import reduce

numbers = [1, 2, 3, 356, 24, 45, 56, 64]
 
even_numbers = filter(lambda x : x % 2 == 0, numbers)
print(list(even_numbers))
