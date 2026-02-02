# Problem 68: Find sum of even indexed elements
# Find and fix the error

def sum_even_indices(lst):
    return sum(lst[::2])

numbers = [1, 2, 3, 4, 5, 6]
result = sum_even_indices(numbers)
print(f"Sum of even indices: {result}")   
