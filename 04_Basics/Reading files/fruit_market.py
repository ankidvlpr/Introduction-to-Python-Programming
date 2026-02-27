# The file fruits.csv contains names of fruits, and their prices, in the format specified in this example:

# banana;6.50
# apple;4.95
# orange;8.0
# ...etc...
# Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents. In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float.

# NB: the function does not take any arguments. The file you are working with is always named fruits.csv.
    
def read_fruits():
    with open("fruits.csv") as file:
        new_dict = {}

        for line in file:
            line = line.strip()
            parts = line.split(";")
            
            name = parts[0]
            price = float(parts[1])
        
            new_dict[name] = price

    return new_dict


if __name__ == "__main__":
    print(read_fruits())

            

