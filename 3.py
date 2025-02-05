def get_max(a, b, c):
    return max(a, b, c)

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))

    maximum = get_max(a, b, c)
    print(f"The maximum number is: {maximum}")
except ValueError:
    print("Please enter valid numbers.")