# List of employee
employeeList = ["Harry", "James" , "John", "Doe", "Novick"]

# Using for loop to print every element of a list 
for employee in employeeList:
    print(employee)

# List of employee with salary
employeeList2 = [["Harry", 20000], ["James", 15000] , ["John", 5000], ["Doe", 6000], ["Novick", 60000]]

for employee, salary in employeeList2:
    print("Salary of", employee ,"is", salary, "Rs.")

# Typecasting employeeList  to dictionary 
dict1 = print(dict(employeeList2))


for employee in dict1:
    print(employee)