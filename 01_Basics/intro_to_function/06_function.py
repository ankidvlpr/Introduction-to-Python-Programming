# Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. 
# The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:


# Sample output
# 101
# 010
# 101

# 101010
# 010101
# 101010
# 010101
# 101010
# 010101

def chessboard(length):
    i = 0
    while i < length:
        j = 0
        line = ""
        while j < length:
            if (i + j) % 2 == 0:
                line += "1"
            else:
                line += "0"
            j += 1
        print(line)
        i += 1


# Testing the function
if __name__ == "__main__":
    chessboard(3)
    print()
    chessboard(6)
