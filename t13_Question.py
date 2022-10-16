# Take input from use unless number lesser than 100 is entered 

print("Enter a number here...")
num = int(input())
while num < 100:
    print("Enter a number here...")
    num = int(input())
print("You have entered a number greater than or equal to 100")