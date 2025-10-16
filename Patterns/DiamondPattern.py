"""
Function to return a diamond pattern of '*' of side n as a list of strings.

Parameters:
n (int): The number of rows for the upper part of the diamond.

Returns:
list: A list of strings where each string represents a row of the diamond.
"""

def generate_diamond(n):
    triangle_list = []
    for i in range(1, n+1):
        star_len = 2 * i - 1
        space_len = n - i
        triangle_list.append(" " * space_len + "*" * star_len + " " * space_len)
    for i in range(n-1, 0, -1):
        star_len = 2 * i - 1
        space_len = n - i
        triangle_list.append(" " * space_len + "*" * star_len + " " * space_len)
    return triangle_list

size = int(input("Enter the size of the triangle: "))
print(generate_diamond(size))