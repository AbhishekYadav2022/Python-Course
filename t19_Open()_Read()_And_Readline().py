# Opening a file 
f = open("file.txt") # Second argument is the mode of the file 
# f = open("file.txt", "rt") # Default 
# f = open("file.txt", "rb") # Reads in binary format 

# Reading a file 
# content = f.read()
# content = f.read(5) # Reads 5 characters 
# print(content)

# content = f.read(5) # ? Important # Reads next 5 characters of the content
# print(content)

# content = f.read(5000) # ? It will read all the characters in the file
# print(content)

# for line in f:
#     print(line, end="") # ? It the content line by line

# print(f.readline(), end="") # ? It will also read the content line by line

# print(f.readline(), end="") # ? It will also read the content line by line

# print(f.readline(), end="") # ? It will also read the content line by line

print(f.readlines()) # ? It will print all the lines in a list with new line character at the end of each line 

# Closing a file 
f.close()