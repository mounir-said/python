# Countdown
def countdown(num):
    return list(range(num, -1, -1))

# Print and Return
def print_and_return(arr):
    print(arr[0])
    return arr[1]

# First Plus Length
def first_plus_length(arr):
    return arr[0] + len(arr)

# Values Greater than Second
def values_greater_than_second(arr):
    if len(arr) < 2:
        return False
    second_value = arr[1]
    new_list = [x for x in arr if x > second_value]
    print(len(new_list))
    return new_list

# This Length, That Value
def length_and_value(size, value):
    return [value] * size

# Test cases
print(countdown(5))  # [5, 4, 3, 2, 1, 0]
print(print_and_return([1, 2]))  # prints 1, returns 2
print(first_plus_length([1, 2, 3, 4, 5]))  # 6
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))  # prints 3, returns [5, 3, 4]
print(values_greater_than_second([3]))  # False
print(length_and_value(4, 7))  # [7, 7, 7, 7]
print(length_and_value(6, 2))  # [2, 2, 2, 2, 2, 2]
