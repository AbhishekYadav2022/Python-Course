# Our function first searches variables in local scope if it does not find it there then it tries it to find out in global scope

i = 10  # Global scope variable

def function1():
    # i = i + 4 # ? Value of global variable can not be updated in a function
    # If we want to update value of global variable inside a function, we can do it by using global keyword 
    global i # Like this
    i = 5  # Local scope variable
    print("This is me", i)

function1()

print(i)

# Second example of global scope # ? Important
def function2():
    x = 49
    def function3():
        global x
        x = 48
    print("Before calling function3", x)
    function3()
    print("After calling function3", x)

function2()
print(x)