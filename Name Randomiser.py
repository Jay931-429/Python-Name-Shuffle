# Imports module
import random

# Opens Text File
mane = open("Names","r+")

# Reads Text File
sesame = mane.readlines()

# Shuffles name in text
random.shuffle(sesame)

# Initializes a list
items = []
# Appends list with randomized selection of names
[items.append(x) for x in sesame if x not in items]

# for loop for the operation
for i in sesame:
    items.append(i)
new_items = [x[:-1] for x in items]

# Determines the amount of items in list
new_items = new_items[:5]

# Prints the list
print(new_items)


    