# Builtin Random Module
import random  # Importing random module

print("Printing a random number...")
random_number = random.randint(0, 5)
print(f"{random_number} is a random number.")

# Printing random element from a list
channelList = ["Hacker News", "Aaj Tak", "Times News", "Hindustan Times"]
choice = random.choice(channelList)
print(choice)

# To install an external module use the following command
# ? pip install module_name
