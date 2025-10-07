"""
Function to return an inverted right-angled triangle of '*' of side n as a list of strings.

Parameters:
n (int): The height and base of the triangle.

Returns:
list: A list of strings where each string represents a row of the triangle.
"""
def generate_inverted_triangle(n):
    triangle_list = []
    for i in range(n,0,-1):
        str = ''
        for j in range(i):
            str += '*'
        triangle_list.append(str)
    return triangle_list

side = int(input("Enter the base and height of the triangle: "))
print(generate_inverted_triangle(side))
for ele in generate_inverted_triangle(side):
    print(ele)