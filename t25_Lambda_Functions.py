# Anonymous or Lambda Functions in Python 

# Named Function
def minus(x, y):
    return x - y

# Calling Named Function 
print(minus(7, 6))

# Lambda Function 
minus = lambda x, y: x - y

# Calling Lambda Function 
print(minus(8, 6))

# Sorting With Lambda Function 

list = [[2,3], [6,3], [13,1], [10,4]]
list.sort(key = lambda x: x[0]) # key takes a function
print(list)