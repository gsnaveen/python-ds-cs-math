def bracesValidator(inStr):
    valid = True
    pairs = {'{':'}','[':']','(':')'}
    stack = []
    
    for char in inStr:
        
        if char in pairs.keys():
            stack.append(char)
        
        elif char in pairs.values():
            if pairs[stack[-1]] != char:
                valid = False
            elif pairs[stack[-1]] == char:
                stack.pop()
    return valid
    
    
inStr = "{[)]}"
bracesValidator(inStr)
