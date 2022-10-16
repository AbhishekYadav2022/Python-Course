# Dictionary is nothing but a key value pairs 
d1 = {}
print (type(d1))

# Dictionary 1
d2 = {"Harry": "Burger", "Rohan": "Fish", "SkillF": "Bread",}
print(d2["Rohan"])

# Dictionary 2
d2 = {"Vivek": "Pie", "Mukesh":{ "Breakfast": "Fish", "Lunch": "Egg", "Night": "Rice"}}
print(d2["Mukesh"]["Lunch"])

# Updating dictionary 
dict4 = {"Vivek": "English", "Mukesh": "Math"} # Favourite Subjects
dict4["Shivam"] = "Physics"
print(dict4["Shivam"]) 

# Deleting item from dictionary 
del dict4["Vivek"]
# print(dict4["Vivek"]) # Error due to deletion 

# Dictionary functions 
## Copy function 
myDict1 = {"Vivek": "Goa", "Mukesh": "Jaipur", "Ravi": "Shrinagar"}
# myDict2 = myDict1 # This will not make a new dictionary # Do not use this to make copy of a dictionary

myDict3 = myDict1.copy() # This will not make a copy of dictionary myDict3 and provide it to myDict1
del myDict3["Mukesh"]

print(myDict1["Mukesh"])
# print(myDict3["Mukesh"]) # This line will throw an error 

## Get function 
print(myDict1.get("Vivek"))

## Update function 
myDict1.update({"Leena": "Mumbai"})
print(myDict1.get("Leena"))

## Keys function
print(myDict1.keys())

## Items function
print(myDict1.items())