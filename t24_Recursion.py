# Recursion In Python

# Iterative Approach 
def factorial(n):

    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact


print("Enter a number here to find out it's factorial:", end=" ")
number = int(input())
print("Factorial:", factorial(number))

# Recursive Approach 

def factorial2(n):
    if n == 1:
        return 1
    else:
        return n*factorial2(n-1)

print("Enter a number here to find out it's factorial:", end = " ")
number2 = int(input())
print("Factorial:", factorial2(number2))

# Fibonacci series # ? 0 1 1 2 3 5 8 13

def fibonacci(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else: 
        return fibonacci(x-1) + fibonacci(x-2)
print("Enter a number here...")
num = int(input())
print("Fibonacci:",fibonacci(num))
