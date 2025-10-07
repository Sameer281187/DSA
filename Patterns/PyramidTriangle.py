"""
Function to return a pyramid pattern of '*' of side n as a list of strings.

Parameters:
n (int): The number of rows in the pyramid.

Returns:
list: A list of strings where each string represents a row of the pyramid.
"""
def generate_pyramid(n):
    triangle_list = []
    for i in range(1, n+1):
        stars = 2 * i - 1
        spaces = n - i
        str = " " * spaces + "*" * stars + " " * spaces
        triangle_list.append(str)
    return triangle_list

size = int(input("Enter the size of the pyramid triangle: "))
print(generate_pyramid(size))
for ele in generate_pyramid(size):
    print(ele)