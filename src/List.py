#Python's list comprehensions provide a concise way to create lists. 
#Although not exclusively a functional programming feature, they are often used in a functional style.

# Example of list comprehension

numbers = [1, 2, 3, 356, 24, 45, 56, 64]

squares = [x**2 for x in numbers]
print(squares)
