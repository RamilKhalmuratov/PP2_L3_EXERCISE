def is_even(number):
    return number % 2 == 0

try:
    user_input = int(input("Enter an integer: "))
    if is_even(user_input):
        print(f"{user_input} is even.")
    else:
        print(f"{user_input} is odd.")
except ValueError:
    print("Please enter a valid integer.")