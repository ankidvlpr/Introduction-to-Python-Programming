# Please write a function named no_vowels, which takes a string argument. 
# The function returns a new string, which should be the same as the original but with all vowels removed.

# You can assume the string will contain only characters from the lowercase English alphabet a...z.

# An example of expected behaviour:

# Sample output
# ths s n xmpl


def no_vowels(sentence: str):
    new_sentence = ""
    
    for char in sentence:
        if char not in "aeiou":
            new_sentence += char

    return new_sentence

if __name__ == "__main__":
    my_string = "this is an example"
    sentence = no_vowels(my_string)
    print(sentence)

