# Sum function # Built-in function 
from ast import arguments


a = 9 
b = 10
c = sum([a,b]) # It's argument must be iterable # Tuple or List
print(c)

# User-defined function
def sayHello():
    print("Hello from function")
    
sayHello()

# Function with arguments
def add(a,b):
    print("Sum =", a+b)

add(2,3)

# Function with return value 
def average(a, b):
    c = sum([a,b])/2
    return c

print("Average =", average(2,3))

# Docstring # ? Important
def function2(a, b):
    """This is a function which will calculate average of two numbers"""
    average = sum([a,b])/2
    return average

print("Average =", function2(12,13)) # Calling function 

print(function2.__doc__) # This will print the doctstring of function2   

print(sum.__doc__) # Printing doctstring of built-in sum function 