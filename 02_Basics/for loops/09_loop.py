# Please write a function named distinct_numbers, which takes a list of integers as its argument.
# The function returns a new list containing the numbers from the original list in order of magnitude,
# and so that each distinct number is present only once.

# my_list = [3, 2, 2, 1, 3, 3, 1]
# print(distinct_numbers(my_list)) # [1, 2, 3]



def distinct_numbers(my_list: list):
    new_list = []
    for item in my_list:
        if item in new_list:
            continue
        new_list.append(item)
        short = sorted(new_list)
    
    return short



if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))