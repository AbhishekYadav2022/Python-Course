# If statement 
var1 = 49
print("Enter a number here...")
var2 = int(input())

if var2 > var1:
    print("Greater")
elif var2 == var1:
    print("Equal")
else: 
    print("Lesser")

# In keyword  
list = [5,6,7]
print(5 in list)
if 5 in list:
    print("Yes it is in the list")

# Not in keyword
print(9 not in list)
if 9 not in list:
    print("No it is not in the list")
