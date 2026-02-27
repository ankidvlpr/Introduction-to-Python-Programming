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