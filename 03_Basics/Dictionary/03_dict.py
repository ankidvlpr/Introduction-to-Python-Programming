# Please write a function named histogram, which takes a string as its argument.
# The function should print out a histogram representing the number of times each letter occurs in the string.
# Each occurrence of a letter should be represented by a star on the specific line for that letter.

# For example, the function call histogram("abba") should print out

# Sample output
# a **
# b **

# while histogram("statistically") should print out

# Sample output
# s **
# t ***
# a **
# i **
# c *
# l **
# y *



def histogram(string: str):
    histogram = {}
    for char in string:
        if char not in histogram:
            histogram[char] = 0
        histogram[char] += 1
    # print(f"{char} ", end="")
    # print(histogram[char]* "*")
    for key in histogram:
        print(key, histogram[key] * "*")

    return key

if __name__ == "__main__":
    word = histogram("statistically")
    print(word)















