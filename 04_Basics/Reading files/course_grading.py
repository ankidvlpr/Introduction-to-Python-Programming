# This program works with two CSV files. One of them contains information about some students on a course:

# id;first;last
# 12345678;peter;pythons
# 12345687;jean;javanese
# 12345699;alice;adder
# The other contains the number of exercises each student has completed each week:

# id;e1;e2;e3;e4;e5;e6;e7
# 12345678;4;1;1;4;5;2;4
# 12345687;3;5;3;1;5;4;6
# 12345699;10;2;2;7;10;2;2
# As you can see above, both CSV files also have a header row, which tells you what each column contains.

# Please write a program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student. If the files have the contents in the examples above, the program should print out the following:

# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# pekka peloton 21
# jaana javanainen 27
# liisa virtanen 35

# Hint: while testing your program, you may quickly run out of patience if you always have to type in the file names at the prompt. You might want to hard-code the user input, like so:

# if False:
#     # this is never executed
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # hard-coded input
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"
# The actual functionality of the program is now "hidden" in the False branch of an if statement. It will never be executed.

# Now, if you want to quickly verify the program works correctly also with user input, you can just replace False with True:


# if True:
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # now this is the False branch, and is never executed
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"
    
    
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

new_dict = {}
with open(student_info) as new_file:

    for line in new_file:
        parts = line.strip().split(";")

        if parts[0] == "id":
            continue
        name = parts[1]
        last = parts[2]
        full_name = name + " "+ last 

        new_dict[parts[0]] = full_name

total_exercise = {}

with open(exercise_data) as file:
    for line in file:
        parts = line.strip().split(";")

        if parts[0] == "id":
            continue
        total_exercise[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])

for id, value in new_dict.items():
    if id in total_exercise:
        total = total_exercise[id]
        print(f"{value} {total}")
    else:
        print("Error")

