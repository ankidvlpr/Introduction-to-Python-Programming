# Please write a function named box_of_hashes, which prints out a rectangle of hash characters. The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.

# The function should call the function linefrom the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in your linefunction.

# Some examples of how the function should work:

# box_of_hashes(5)
# print()
# box_of_hashes(2)

#     Sample output
#     ##########
#     ##########
#     ##########
#     ##########
#     ##########

#     ##########
#     ##########

def line(length,ch):
    i = 0
    while length > i:
        if ch == "":
            print("#",end="")
        else:
            print(ch[0], end="")
        i += 1
    print()

def box_of_hashes(height):
    k = 0
    while k < height:
        line(10, "#")
        k += 1
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)
