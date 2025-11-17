"""
Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.

Parameters:
n (int): The height of the triangle.

Returns:
list: A list of strings where each string represents a row of the triangle.
"""

def generate_hollow_inverted_right_angled_triangle(n):
    triangle_list = []
    for i in range(n, 0, -1):
        if i < 3 or i == n:
            triangle_list.append("*" * i)
        else:
            triangle_list.append(f"*{" " * (i-2)}*")
    return triangle_list

size = int(input("Enter the size of the triangle: "))
print(generate_hollow_inverted_right_angled_triangle(size))