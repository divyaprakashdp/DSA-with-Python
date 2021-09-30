
def isValid(input):
    bracketStack = []
    for char in input:
        if char in ['[', '{', '(']:
            bracketStack.append(char)
        elif (char==')' and not bracketStack and bracketStack[-1]=='(') or (char=='}' and not bracketStack and bracketStack[-1]=='{') or (char==']' and not bracketStack and bracketStack[-1]=='['):
            bracketStack.pop()
        else:
            return False
    return bracketStack





print(isValid("()"))