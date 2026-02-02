# Problem 81: Check if string has balanced brackets
# Find and fix the error

def balanced_brackets(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

expr = "{[()]}"
print(f"Balanced: {balanced_brackets(expr)}")    
