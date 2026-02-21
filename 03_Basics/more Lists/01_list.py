# Please write a function named longest(strings: list), which takes a list of strings as its argument. 
# The function finds and returns the longest string in the list. 
# You may assume there is always a single longest string in the list.

# Sample output
# howdydoody



def longest(strings: list):
    new_list = []
    longest = 0
    for char in strings:
        if len(char) > longest:
            longest = len(char)
            new_list = char
    return new_list
        

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))