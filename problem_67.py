# Problem 67: Remove nth element from list
# Find and fix the error

def remove_nth(items, n):
    if 0 <= n < len(items):
        return items[:n] + items[n+1:]
    return items

numbers = [1, 2, 3, 4, 5]
result = remove_nth(numbers, 2)
print(f"After removing: {result}")   
