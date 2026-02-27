# The file numbers.txt contains integer numbers, one number per line. The contents could look like this:

# 2
# 45
# 108
# 3
# -10
# 1100
# ...etc...
# Please write a function named largest, which reads the file and returns the largest number in the file.



def largest():
    largest = None
    with open("numbers.txt") as new_file:
        
        for content in new_file:
            number = int(content.strip())
            if largest is None or number > largest:
                largest = number


    return largest 

if __name__ == "__main__":
    read = largest()
    print(read)