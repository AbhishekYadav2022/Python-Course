# File Pointer 
f = open("file2.txt")
print(f.tell()) # ? It will tell us where is our file pointer or handler
print(f.readline())
f.seek(5) # ? It will set our file pointer to desired character
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.close()