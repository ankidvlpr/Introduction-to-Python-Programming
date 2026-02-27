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

            

