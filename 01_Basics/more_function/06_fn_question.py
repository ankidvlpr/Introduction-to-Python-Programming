# Please write a function named shape, which takes four arguments. 
# The first two parameters specify a triangle, as above, and the character used to draw it.
#  The first parameter also specifies the width of a rectangle, while the third parameter specifies its height.
#  The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle,
#   and then the rectangle below it.
# Some examples:

    # shape(5, "X", 3, "*")
    # print()
    # shape(2, "o", 4, "+")
    # print()
    # shape(3, ".", 0, ",")
    # Sample output
    # X
    # XX
    # XXx
    # XXXX
    # XXXXX
    # *****
    # *****
    # *****

def line(size, character):
    print(character[0] * size)

def shape(width, triangle_char, rectangle_height, rectangle_char):
    i = 1
    while i <= width:
        line(i, triangle_char)
        i += 1
    k = 1
    while k <= rectangle_height:
        line(width, rectangle_char)
        k += 1


if __name__ == "__main__":
    shape(5, "x", 3, "*")