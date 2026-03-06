# The file solutions.csv contains some solutions to mathematics problems:

# Arto;2+5;7
# Pekka;3-2;1
# Erkki;9+3;11
# Arto;8-3;4
# Pekka;5+5;10
# ...jne...
# As you can see above, on each line the format is name_of_student;problem;result. All the operations are either addition or subtraction, and each has exactly two operands.

# Please write a function named filter_solutions() which

# Reads the contents of the file solutions.csv
# writes those lines which have a correct result into the file correct.csv
# writes those lines which have an incorrect result into the file incorrect.csv
# Using the example above, the file correct.csv would contain the lines

# Arto;2+5;7
# Pekka;3-2;1
# Pekka;5+5;10
# The other two would be in the file incorrect.csv.

# Please write the lines in the same order as they appear in the original file. Do not change the original file.



def filter_solutions():

    with open("solutions.csv") as new_file, \
         open("correct.csv", "w") as correct, \
         open("incorrect.csv", "w") as incorrect:

        for line in new_file:

            line = line.strip()

            parts = line.split(";")

            problem = parts[1]
            solution = int(parts[2])

            if "+" in problem:

                a, b = problem.split("+")
                result = int(a) + int(b)

            else:

                a, b = problem.split("-")
                result = int(a) - int(b)

            if result == solution:

                correct.write(line + "\n")

            else:

                incorrect.write(line + "\n")
                

if __name__ == "__main__":
    print(filter_solutions())