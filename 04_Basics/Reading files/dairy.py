# Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. When the program is executed, it should first read any entries already in the file.

# NB: the automatic tests for this exercise will change the contents of the file. If you want to keep its contents, first make a copy of the file under a different name.

# The program should work as follows:

# Sample output
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: Today I ate porridge
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: I went to the sauna in the evening
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!

# When the program is executed for the second time, this should happen:

# Sample output
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!



print("1 - add an entry, 2 - read entries, 0 - quit")


while True:
    function = int(input("Function: "))

    if function == 0:
        print("Bye now!")
        break
    elif function == 1:
        entry = input("Dairy entry: ")

        with open("diary.txt", "a") as new_file:
            new_file.write(entry + "\n")

        print("Dairy saved")
            
        
    elif function == 2:
        with open("diary.txt", "r") as new_file:
            print(new_file.read())

