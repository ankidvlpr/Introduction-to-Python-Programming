# Please write a program which first asks the user for the number of items to be added. Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out.

# An example of expected behaviour:

# Sample output
# How many items: 3
# Item 1: 10
# Item 2: 250
# Item 3: 34
# [10, 250, 34]








# blank = []
# store = int(input("How many items: "))
# i = 1
# while i <= store:
#     print(f"Item {i}: {store} ")
#     blank = blank + store + " "
#     i += 1
# print(blank)

# this is one of my failure attempt the journey is very exiciting


blank = []
store = int(input("How many items: "))

i = 1
while i <= store:
    value = int(input(f"Item {i}: "))
    blank.append(value)
    i += 1

print(blank)



