# *args and **kwargs in Python 

# Without Args 
def student_name(a, b, c, d, e, f):
    print(a, b, c, d, e, f)

student_name("Rohan", "Sohan", "Ravi", "Vivek", "Suresh", "Deena")

# With Args 
def employee_name(*args):
    for item in args:
        print(item)

employees = ["Ramu", "Killer", "Nikhil", "John", "Pnan", "Deena", "The Programmer", "The Hacker"]

employee_name(*employees) # ? Important # Here our list goes to function as a tuple either you have passed it as a list or tuple 

# With Args And A Normal Argument  
def employee_name2(me, *args): # ? Normal argument must be before *args 
    print(me)
    for item in args:
        print(item)

me = "Abhishek"
employees2 = ["Ramu2", "Killer2", "Nikhil2", "John2", "Pnan2", "Deena2", "The Programmer2", "The Hacker2"]

employee_name2(me, *employees2) 

# With Normal Argument, Args and Kwargs 
def numbers_function(my, *args, **kwargs): # Order must be this
    print(my)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(key, value)
        
my = 7
fav_num = [1, 6, 9, 3, 5]
fav_num_dict = {"Rohan": "56", "John": "86", "Ravi": "77"}
numbers_function(my, *fav_num, **fav_num_dict)