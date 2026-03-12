# Please write a function named lottery_numbers(amount: int, lower: int, upper: int), 
# which generates as many random numbers as specified by the first argument.
# All numbers should fall within the bounds lower to upper. 
# The numbers should be stored in a list and returned. 
# The numbers should be in ascending order in the returned list.

# As these are lottery numbers, no number should appear twice in the list.

# An example of how the function should work:

# for number in lottery_numbers(7, 1, 40):
#     print(number)
# Sample output
# 4
# 7
# 11
# 16
# 22
# 29
# 38

from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    new_list = []
    '''Generate random lottery numbers'''
    
    for i in range(amount):
        lottery = randint(lower,upper)

        while lottery in new_list:
            lottery = randint(lower,upper)

        new_list.append(lottery)

    ascending = sorted(new_list)  
    return ascending

if __name__ == "__main__":
    result = lottery_numbers(7,1,40)
    
    for num in result:
        print(num)




        
