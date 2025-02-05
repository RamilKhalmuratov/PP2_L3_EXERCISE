def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the position of the Fibonacci number you want: "))
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")