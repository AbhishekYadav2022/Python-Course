# Try exception handling 
print("Enter num 1")
num1 = input()

print("Enter num 2")
num2 = input()

# Try Exception 
try:
    print("Sum of the numbers is", sum[int(num1), int(num2)])
except Exception as e:
    print("Error:",e)

print("This line is very important")
