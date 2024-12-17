def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    
    # Input validation: Check if all elements are numbers
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("List must contain only numbers.")
            
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example Usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

# Example with error handling
try:
    my_numbers = [10, 20, 'a']
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")
except TypeError as e:
    print(f"Error: {e}")
