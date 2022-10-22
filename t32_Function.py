# These function are used in another file 
# Function 1
def print_something(string):
    return f"This is something. {string}"

# Function 2
def add(num1, num2):
    return num1 + num2 + 5

# Printing Something 
print("This is outside main function.")

# Printing name==main 
print("Name is", __name__)

# name==main starts here 
if __name__ == "__main__":
    # Anything 
    print(print_something("Vow!"))
    print("This is inside main function.")
