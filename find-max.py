# Test List of Numbers 

numbers = [1, 45.5, -5, 9]

# For Loop

def find_max(numbers):
    if len(numbers) == 0:
        print("no numbers")
        return None
    
    curr_max = numbers[0]
    for num in numbers:
        if num >= curr_max:
            curr_max = num
    print(curr_max)
    return curr_max

# While Loop

def find_max_while_loop(numbers):
    if len(numbers) == 0:
        print("no numbers")
        return None
    
    i = 0 
    curr_max = numbers[0]
    
    while i < len(numbers) - 1:
        i += 1 
        if numbers[i] >= curr_max:
            curr_max = numbers[i]
    print(curr_max)
    return curr_max

# Call Functions

find_max(numbers)
find_max_while_loop(numbers)