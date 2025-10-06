"""
Function to return a hollow square pattern of '*' of side n as a list of strings.

Parameters:
n (int): The size of the square.

Returns:
list: A list of strings where each string represents a row of the hollow square.
"""
def generate_string(n):
    str = ""
    for _ in range(n):
        str += '*'
    return str

def generate_hollow_string(n):
    str = ""
    for i in range(n):
        if i == 0 or i == n-1:
            str += '*'
        else:
            str += ' '
    return str

def generate_hollow_square(n):
    sq_list = []
    for i in range(n):
        if i == 0 or i == n-1:
            sq_list.append(generate_string(n))
        else:
            sq_list.append(generate_hollow_string(n))
    return sq_list

size = int(input("Enter the size of the square: "))

print(generate_hollow_square(size))