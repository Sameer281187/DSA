def generate_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

generate_pyramid(7)