def isValid(s: str) -> bool:
    stack = []
    char_map = {
        ')': '(', 
        ']': '[', 
        '}': '{'
    }

    for char in s:
        if char in char_map:
            top = stack.pop() if stack else '#'
            if char_map[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

    