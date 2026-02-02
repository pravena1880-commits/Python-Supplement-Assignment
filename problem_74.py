# Problem 74: Find first non-repeating character
# Find and fix the error

def first_non_repeating(text):
    char_count = Counter(text)
    for char in text:
        if char_count[char] == 1:
            return char
        return None

word = "programming"
result = first_non_repeating(word)
print(f"First non-repeating: {result}")    
