# Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value of the three.

# An example of how the function is used:

# print(greatest_number(3, 4, 1)) # 4
# print(greatest_number(99, -4, 7)) # 99
# print(greatest_number(0, 0, 0)) # 0


def greatest_number(a,b,c):
    if a >= b and a >= c:
        return a
    elif a <= b and b >= c:
        return b
    elif a <= c and b <= c:
        return c
    if a == b == c:
        return 1

if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)