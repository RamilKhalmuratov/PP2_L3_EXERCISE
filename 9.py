def calculate_running_average(numbers):
    running_average = []
    total = 0
    
    for i, num in enumerate(numbers):
        total += num
        average = total / (i + 1)
        running_average.append(average)
        
    return running_average

input_numbers = input("Enter numbers separated by spaces: ")
number_list = list(map(float, input_numbers.split()))

running_averages = calculate_running_average(number_list)
print("Running averages:", running_averages)