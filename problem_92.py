# Problem 92: Check if all elements are unique
# Find and fix the error

def all_unique(lst):
    seen = []
    for item in lst:
        if item in seen:
            return False
        seen.append(item)
    return True

numbers = [1, 2, 3, 4, 5]
print(f"All unique: {all_unique(numbers)}")  
