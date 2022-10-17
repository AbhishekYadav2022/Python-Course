from re import A


# With block is also to read and write # ? Important 
# We do not need to close after reading with with block 
with open("file2.txt") as f:
    a = f.read(5)
    print(a)