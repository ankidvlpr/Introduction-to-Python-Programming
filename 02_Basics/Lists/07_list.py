# Please write a function named mean, which takes a list of integers as an argument. 
# The function returns the arithmetic mean of the values in the list.

# my_list = [1, 2, 3, 4, 5]
# result = mean(my_list))
# print("mean value is", result)
# Sample output
# mean value is 3.0

def mean(my_list: list):
    add = sum(my_list)
    i = 0
    while i < len(my_list):
        i += 1
    arthmetic_mean = add/i
    return arthmetic_mean

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print("mean value is", result)