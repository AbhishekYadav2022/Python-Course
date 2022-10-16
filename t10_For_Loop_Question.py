# Print every number of list that is greater than 2

list = ["Shivam", "A", 59, "B", 5, "C", 20]

for item in list:
    if str(item).isnumeric() and item > 1:
        print(item)