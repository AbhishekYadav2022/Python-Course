# Break and continue in python 
i = 0

# While 1 and while true are infinite loops 
while(i < 6000):
    if i+1 < 4000: 
        i += 1
        continue
    print(i)
    if(i == 4010):
        break # Stop the loop
    i += 1