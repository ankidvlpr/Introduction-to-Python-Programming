# Please write a function named print_many_times(text, times), which takes a string and an integer as arguments.
# The integer argument specifies how many times the string argument should be printed out:

# print_many_times("hi", 5)

# print()

# text = "All Pythons, except one, grow up"
# times = 3
# print_many_times(text, times)
def print_many_times(text, times):
    i = 0
    while i < times:
        print(text)
        i += 1

if __name__ == "__main__":
    print_many_times("hi", 5)
    print_many_times("All Pythons, except one, grow up.", 3)