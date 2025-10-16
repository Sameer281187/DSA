"""
Function to return a sandglass pattern of '*' of side n as a list of strings.

Parameters:
n (int): The height of the sandglass.

Returns:
list: A list of strings where each string represents a row of the sandglass pattern.
"""
def generate_sandglass(n):
    triangle_list = []
    for i in range(n, 0, -1):
        triangle_list.append((n-i) * " " + (2*i-1) * "*" + (n-i) * " ")

    for i in range(2, n+1):
        triangle_list.append((n-i) * " " + (2*i-1) * "*" + (n-i) * " ")

    return triangle_list

size = int(input("Enter the size of the triangle: "))
print(generate_sandglass(size))