# Using Enumerate Function In Python
# We can use enumerate function with list or tuple
list = ["Potato", "Tomato", "Carrot", "Radish"]
for index, item in enumerate(list):
    if index % 2 == 0:
        print(index, item)