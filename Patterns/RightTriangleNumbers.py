"""
Function to return a right-angled triangle of repeated numbers of side n as a list of strings.

Parameters:
n (int): The height of the triangle.

Returns:
list: A list of strings where each string represents a row of the triangle.
"""
def generate_number_triangle(n):
    triangle_list = []
    for i in range(1, n + 1):
        string = str(i) * i
        triangle_list.append(string)
    return triangle_list

size = int(input("Enter the size of the triangle: "))
print(generate_number_triangle(size))
for ele in generate_number_triangle(size):
    print(ele)