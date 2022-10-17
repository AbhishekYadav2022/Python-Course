# Operators in python 

## Arithmetic Operators 
from traceback import print_tb


print("5 + 5 =", 5+5)
print("5 - 5 =", 5-5)
print("5 * 5 =", 5*5)
print("5 / 5 =", 5/5)
print("5 // 5 =", 5//5) # Important # It returns integer value
print("5 % 5 =", 5%5)

## Assignment Operators 
x = 5
print(x)
x += 4
print(x)
x /= 4
print(x)
x -= 4
print(x)
x *= 4
print(x)
x %= 5 # Important # It means x = x % 5
print(x)

# Comparison Operators 
i = 5
print(i == 8)
print(i != 8)
print(i <= 8)
print(i >= 8)

# Logical Operators
a = True
b = False

print( a and b)
print( a or b)

# Identity Operators 
print(a is b)
print(a is not b)
print(a is not True)

# Membership Operators 
list = [1, 2, 3, 4, 5, 6, 7]
print(5 in list)
print(48 in list)
print(48 not in list)

# Bitwise Operators #? Important
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 1)
print(0 | 1)
print(0 & 3)
print(0 | 3)