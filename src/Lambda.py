"""lambda takes a number of parameters and an expression combining these parameters,
 and creates an anonymous function that returns the value of the expression."""

# Example of a lambda function
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6

def multiply(x,y):
    x * y

add = lambda x, y : x + y
print(add(10,20))

def adder(x, y):
    return x + y

subtract = lambda x, y : x - y
print(subtract(10,7))

def subtract(x,y):
    x - y

divide = lambda x, y : x / y
print(divide(100,2))

def divide(x,y):
    x / y


print_assign = lambda name, value: name + '=' + str(value)
print(print_assign('Uk', 'London'))

my_list = ['apple', 'banana', 'cherry', 'date']
sorted_list = sorted(my_list, key=lambda x: len(x))
print(sorted_list) 

