"""
Function to return the first n rows of Floyd's Triangle as a list of strings.

Parameters:
n (int): The number of rows in the triangle.

Returns:
list: A list of strings where each string represents a row of Floyd's Triangle.
"""
def generate_floyds_triangle(n):
    triangle_list = []
    counter = 1
    for i in range(1, n+1):
        stro = ""
        for j in range(i):
            stro += str(counter)
            counter += 1
            if j+1 in range(i):
                stro += " "
        triangle_list.append(stro)
    return triangle_list

size = int(input("Enter the size of the triangle: "))
print(generate_floyds_triangle(size))