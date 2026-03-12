# Let's have a look at a JSON file, which contains some information about students in the following format:

# [
#     {
#         "name": "Peter Pythons",
#         "age": 27,
#         "hobbies": [
#             "coding",
#             "knitting"
#         ]
#     },
#     {
#         "name": "Jean Javanese",
#         "age": 24,
#         "hobbies": [
#             "coding",
#             "rock climbing",
#             "reading"
#         ]
#     }
# ]
# Please write a function named print_persons(filename: str), which reads a JSON file in the above format,
# and prints the contents as shown below. The file may contain any number of entries.

# Sample output
# Peter Pythons 27 years (coding, knitting)
# Jean Javanese 24 years (coding, rock climbing, reading)

import json

def print_persons(filename: str):
    ''' opening json file and print name age and hobbies'''
    with open(filename) as new_file:
        data = new_file.read()
    
    detail = json.loads(data)

    for info in detail:
        hobbies = ", ".join(info["hobbies"])
        print(f"{info['name']} {info["age"]} years ({hobbies})")

if __name__ == "__main__":
    file = print_persons("file1.json")
    print(file)
    