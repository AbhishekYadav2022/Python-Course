# Writing and appending to a file in python

## ? Creating and writing content to a file using python  
# f = open("file2.txt", "w")
# f.write("Hello, world!")
# f.close()

## ? Appending content to a file using python  
# f = open("file2.txt", "a")
# f.write("Hello, world! ")
# f.close()

## ? Appending content to a file using python  
# f = open("file2.txt", "a")
# a = f.write("Hello, world! ")
# print("Number of characters written:", a) # It will return the number of characters written in the file
# f.close()

# Handling read and write both 
f = open("file2.txt", "r+")
print(f.read()) # Reading
f.write("Thank you!\n") # Writing