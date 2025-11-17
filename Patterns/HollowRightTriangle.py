"""
Function to return a hollow right-angled triangle of '*' of side n as a list of strings.

Parameters:
n (int): The height of the triangle.

Returns:
list: A list of strings where each string represents a row of the triangle.
"""
def generate_hollow_right_angled_triangle(side):
    triangle_list = []

    for i in range(1, side + 1):
        if i < 3 or i == side:
            triangle_list.append(i * "*")
        else:
            triangle_list.append(f"*{" " * (i - 2)}*")
    return triangle_list

size = int(input("Enter the size of the triangle: "))
print(generate_hollow_right_angled_triangle(size))