mystr = "There lived an old man in a hut"
print(mystr)

# Slicing
print(mystr[4]) # Rule 1
print(mystr[0:5]) # Rule 2
print(len(mystr)) # Rule 3
print(mystr[0:31]) # Rule 4
print(mystr[0:60]) # Rule 5
print(mystr[0:20:2]) # Rule 6 # It skips one character
print(mystr[:31]) # Rule 7 # It starts from zero by default
print(mystr[3:]) # Rule 8 # It ends to the last character by default
print(mystr[:]) # Rule 9
print(mystr[::]) # Rule 10
print(mystr[::2]) # Rule 11
print(mystr[-4:-2]) # Rule 12
print(mystr[::-1]) # Rule 13
print(mystr[::-2]) # Rule 13

# Some functions 
print(mystr.isalpha()) # Function 1
print(mystr.isalnum()) # Function 2
print(mystr.endswith("t")) # Function 3
print(mystr.count("a")) # Function 4
print(mystr.capitalize()) # Function 5
print(mystr.find("d")) # Function 6
print(mystr.lower()) # Function 7
print(mystr.upper()) # Function 8
print(mystr.replace("lived", "lives")) # Function 9