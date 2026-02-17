# Please write a function named anagrams, which takes two strings as arguments. 
# The function returns True if the strings are anagrams of each other.
# Two words are anagrams if they contain exactly the same characters.

# Some examples of how the function should work:

# print(anagrams("tame", "meta")) # True
# print(anagrams("tame", "mate")) # True
# print(anagrams("tame", "team")) # True
# print(anagrams("tabby", "batty")) # False
# print(anagrams("python", "java")) # False
# Hint: the function sorted can be used on strings as well.



def anagrams(str1: str, str2: str):
    variable1 = sorted(str1)
    variable2 = sorted(str2)
    if variable1 == variable2:
        return True
    return False



if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java"))