"""
Function to return a right-angled triangle of '*' of side n as a list of strings.

Parameters:
n (int): The height of the triangle.

Returns:
list: A list of strings where each string represents a row of the triangle.
"""

def generate_right_angled_triangle(n):
    triangle_list = []
    for i in range(1, n+1):
        triangle_list.append((n - i) * " " + i * "*")
    return triangle_list

size = int(input("Enter the size of the triangle: "))
print(generate_right_angled_triangle(size))