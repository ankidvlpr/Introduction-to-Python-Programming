# Please write a program which asks the user for words.  in a word for the second time,If the user types 
# the program should print out the number of different words typed in, and exit.

# Sample output
# Word: once
# Word: upon
# Word: a
# Word: time
# Word: upon
# You typed in 4 different words


word = []
while True:
    user = input("Word: ")

    if user in word:
        print(f"You typed in {len(word)} different words")
        break
    else:
        word.append(user)