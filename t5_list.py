# These are lists 
grocery = ["Harpic", "Vim bar", "Deodrant", "Rice","Pulse"]
print(grocery)
print(grocery[3])

numbers = [11, 21, 13, 41, 25, 61, 70]
print(numbers)
# numbers.sort() # It sorts the original numbers list
print(numbers)
# numbers.reverse() # Reverse the original numbers list
print(numbers)
print(numbers[::2])
print(numbers[::-1])
print(len(numbers))
print(max(numbers))
print(min(numbers))

# Adding items to list 
numbers.append(4)
print(numbers)

# Insert Function 
numbersList = [10, 20, 30, 40, 50]
print(numbersList)
numbersList.insert(2, 10)
print(numbersList)

# Remove Function 
numbersList.remove(20)
print(numbersList)

# Pop Function 
numbersList.pop()
print(numbersList)

# Canging the numbers of the list 
numbersList[2] = 500 # Lists are mutable
print(numbersList)