def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    """Function to filter and return only prime numbers from the list."""
    return [num for num in numbers if is_prime(num)]

# Example usage
input_numbers = input("Enter numbers separated by spaces: ")
number_list = list(map(int, input_numbers.split()))

prime_numbers = filter_prime(number_list)
print("Prime numbers from the list:", prime_numbers)