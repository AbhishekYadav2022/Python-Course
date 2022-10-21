# F-Strings in Python 

# Fist approach of formatting a string 
me = "Abhishek"
message = "This is %s" %me
state = "Uttarakhand"
message2 = "This is %s from %s" % (me, state)
print(message)
print(message2)

# Second apprach of formatting a string 

template = "I study in class {} and my roll number is {}."
st1_class = 5
st1_roll = 6
student1 = template.format(st1_class, st1_roll)
print(student1)
st2_class = 4
st2_roll = 10
student2 = template.format(st2_class, st2_roll)
print(student2)

# Third approach of formatting a string - Using F-strings 

guest1 = "Rohan"
guest2 = "Mohan"
place1 = "Jaipur"
place2 = "Kashmir"

print(f"Hello {guest1}! and Welcome to {place1}")
print(f"Hello {guest2}! and Welcome to {place2}")
