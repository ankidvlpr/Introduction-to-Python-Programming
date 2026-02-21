# Please write a function named all_the_longest, which takes a list of strings as its argument.
# The function should return a new list containing the longest string in the original list. 
# If more than one are equally long, the function should return all of the longest strings.

# The order of the strings in the returned list should be the same as in the original.


def all_the_longest(my_list: list):
    max_word = 0
    new_list = []
    for item in my_list:
        if len(item)  > max_word:
            max_word = len(item)

    for item in my_list:
        if max_word == len(item):
            new_list.append(item)

    return new_list

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) 
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result)

