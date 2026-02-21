# Please write a function named most_common_character, which takes a string argument. 
# The function returns the character which has the most occurrences within the string. 
# If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

# An example of expected behaviour:




def most_common_character(string: str):
    max_count = 0
    most_common = ""

    for item in string:
        
        count = string.count(item)

        if count > max_count:
            max_count = count
            max_common = item

    return max_common

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
