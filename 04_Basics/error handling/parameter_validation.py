# Please write a function named new_person(name: str, age: int), 
# which creates and returns a tuple containing the data in the arguments. 
# The first element should be the name and the second the age.

# If the values stored in the parameter variables are not valid, the function should throw a ValueError exception.

# Invalid parameters in this case include:

# name is an empty string
# name contains less than two words
# name is longer than 40 characters
# age is a negative number
# age is greater than 150

def new_person(name: str, age: int):
    if name == "":
        raise ValueError("The name is a empty string")
    elif len(name.split()) < 2:
        raise ValueError("name contain less than two words")
    elif len(name) > 40:
        raise ValueError("name is longer than 40 charcter")
    elif age < 0:
        raise ValueError("age is a negative number")
    elif age > 150:
        raise ValueError("age is greater than 150")


    return (name, age)

if __name__ == "__main__":
    n = new_person("Ankit",19)
    print(n)
    