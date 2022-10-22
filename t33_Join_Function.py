# Join Function In Python 

list = ["John", "Cena", "Rany", "Orton", "Sheamus", "Khali", "Jinder Mahal"]

# Using for loop to print the name of all stars with and at the end of every name 
for item in list:
    print(item, "and", end=" ")
print("Others")

# Doing the same deed using join function 
a = " and ".join(list)
print(a, "Others")