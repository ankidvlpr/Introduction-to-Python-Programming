# The file matrix.txt contains a matrix in the format specified in the example below:

# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc...
# Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.

# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. For example, calling row_sums when the matrix in the file is defined as

# 1,2,3
# 2,3,4
# the function should return the list [6, 9].

def matrix_sum():
    with open("matrix.txt") as file:
        total_sum = 0

        for line in file:   
            parts = line.strip().split(",")

            for item in parts:
                number = int(item)
                total_sum += number

    return total_sum

def matrix_max():
    with open("matrix.txt") as new_file:
        max_num = None

        for line in new_file:
            parts = line.strip().split(",")

            for item in parts:
                num = int(item)
                
                if max_num  is None or num > max_num:
                    max_num = num

    return max_num

def row_sums():
    with open("matrix.txt") as new_file:
        new_list = []
        for line in new_file:
            row_sum = 0
            parts = line.strip().split(",")

            for item in parts:
                num = int(item)
                row_sum += num
                
            new_list.append(row_sum)

    return new_list



            

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
