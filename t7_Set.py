# Set in python 
s = set()
print(type(s))

# Making set from list 
s_from_list = set([1,2,3,4,5])
print(s_from_list)
print(type(s_from_list))

# Or we can make a set like this 
list_of_pet_animals = ["Dog", "Cat", "Cow", "Goat"]
s_of_pet_animals = set(list_of_pet_animals)
print(type(s_of_pet_animals))
print(s_of_pet_animals)

# Adding elements to a set 
s_of_pet_animals.add("Buffalo")
print(s_of_pet_animals)

# Removing elements from a set
s_of_pet_animals.remove("Buffalo")

# Union of sets 
s_of_wild_animals = set(["Lion", "Tiger",])
s_of_animals = s_of_pet_animals.union(s_of_wild_animals)
print(s_of_animals)

# Intersection of sets 
num_set1 = set([1,2,3])
num_set2 = num_set1.intersection([2,3,4])
print(num_set2)
