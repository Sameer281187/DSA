"""
Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.

Parameters:
n (int): The number of rows in the rectangle.
m (int): The number of columns in the rectangle.

Returns:
list: A list of strings where each string represents a row of the rectangle pattern.
"""

def generate_rectangle(n, m):
    rect_list = []
    for i in range(n):
        str = ""
        for j in range(m):
            str += '*'
        rect_list.append(str)
    return rect_list

len = int(input("Enter the length of the rectangle: "))
bre = int(input("Enter the breadth of the rectangle: "))
print(generate_rectangle(len, bre))