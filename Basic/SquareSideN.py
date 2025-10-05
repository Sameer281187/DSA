"""
Function to return a square pattern of '*' of side n as a list of strings.

Parameters:
n (int): The size of the square.

Returns:
list: A list of strings where each string represents a row of the square.
"""

def generate_square(n):
    sq_list = []
    for _ in range(n):
        str = ""
        for _ in range(n):
            str += '*'
        sq_list.append(str)
    return sq_list

size = int(input("Enter the size of the square: "))

print(generate_square(size))

