# Tuples are immutable
# This is how we makes tuple
tp = (1, 2, 3, 4, 5)
print(tp)
print(tp[0])

# Swapping two numbers
a = 1
b = 2
print(a, b)
# Traditional way 
temp = a
a = b
b = temp
print(a, b)
# But in python 
a, b = b, a
print(a, b)