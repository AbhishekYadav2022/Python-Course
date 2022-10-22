# Using Time Module in Python 
import time

# For Loop 
initial = time.time()
print(initial) # Starting Time
for i in range(45):
    print(i)
final = time.time()
print(final) # Ending Time
print(f"Time Taken: {final - initial}") # Time Taken

# While Loop 
initial2 = time.time()
print(initial2) # Starting Time
k = 0   
while (k < 45):
    print(k)
    k += 1
final2 = time.time()
print(final2) # Ending Time
print(f"Time Taken: {final2 - initial2}") # Time Taken

# Conclusion 
print(f"Time Taken By For Loop: {final - initial}")
print(f"Time Taken By While Loop: {final2 - initial2}")

# Pausing the execution of python code for a definite time using time module  
time.sleep(3) # It stops the execution for 3 seconds


# Printing Local Time Using Time Module 
localtime = time.asctime(time.localtime(time.time()))
print(f"Time: {localtime}")