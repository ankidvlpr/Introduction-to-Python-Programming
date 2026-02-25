# Please write a function named invert(dictionary: dict), 
# which takes a dictionary as its argument.
# The dictionary should be inverted in place so that values become keys and keys become values.

# An example of its use:

# Sample output
# {"first": 1, "second": 2, "third": 3, "fourth": 4}

# NB: the principles regarding lists covered here also hold for dictionaries passed as arguments.

# If you have trouble completing this exercise, 
# The visualisation tool might help you understand what your code is or isn't doing.


def invert(dictionary: dict):

    new_dict = {}

    for key in dictionary:
        value = dictionary[key]
        new_dict[value] = key

    dictionary.clear()
    dictionary.update(new_dict)


def main():
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
if __name__ == "__main__":
    main()