# Please write a function named length_of_longest, which takes a list of strings as its argument. 
# The function returns the length of the longest string.

def length_of_longest(my_list):
    max_length = 0

    for item in my_list:
        if len(item) > max_length:
            max_length = len(item)

    return max_length




if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)



