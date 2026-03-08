# The file lottery_numbers.csv containts winning lottery numbers in the following format:

# Sample data
# week 1;5,7,11,13,23,24,30
# week 2;9,13,14,24,34,35,37
# ...etc...

# Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 inclusive.

# The file has been corrupted. Lines in the file may contain the following kinds of errors (these exact lines may not be present in the file, but errors in a similar format will be):

# The week number is incorrect:

# Sample data
# week zzc;1,5,13,22,24,25,26

# One or more numbers are not correct:

# Sample data
# week 22;1,**,5,6,13,2b,34

# Too few numbers:

# Sample data
# week 13;4,6,17,19,24,33

# The numbers are too small or large:

# Sample data
# week 39;5,9,15,35,39,41,105

# The same number appears twice:

# Sample data
# week 41;5,12,3,35,12,14,36

# Please write a function named filter_incorrect(), which creates a file called correct_numbers.csv. The file should contain only those lines from the original file which are in the correct format.


def filter_incorrect():
    with open("lottery_numbers.csv") as new_file, open("correct_numbers.csv", "w") as file:

        for line in new_file:

            line = line.strip()
            parts = line.split(";")
            if len(parts) != 2:
                continue

            week_info = parts[0].split()

            if len(week_info) != 2 or week_info[0] != "week":
                continue

            try:
                int(week_info[1])
            except:
                continue

            numbers = parts[1].split(",")
            if len(numbers) != 7:
                continue
            
            valid = True
            unique = set()

            for number in numbers:
                try:
                    number = int(number)
                except:
                    valid = False
                    break
                
                if number < 1 or number > 39:
                    valid = False
                    break

                if number in unique:
                    valid = False
                    break

                unique.add(number)
            
            if valid:
                file.write(line + "\n")

if __name__ == "__main__":
    filter_incorrect()