# This uses the index of opening brackets and try to match the closing.
# have used the queue for matching the paranthesis and used orddered dict to  check the break in sequence

from collections import deque, OrderedDict
def paran(inStr):
    dq = deque()
    myMatch =  OrderedDict()
    lengthOf = 0
    maxLengthOf = 0
    openB = True;lastIndex = 0
    for index,char in enumerate(inStr):
        
        if char == "(":
            dq.append(index)
            myMatch[index] = -1
        elif dq and char == ")":
            myMatch[dq.pop()] = index
        elif  char == ")":
            myMatch[index] = -2
            

    for key in myMatch.keys():
        
        if myMatch[key] not in (-1,-2):
            lengthOf += 2
            maxLengthOf = max(maxLengthOf,lengthOf)
        else:
            lengthOf = 0 
        
#     print(maxLengthOf)
#     print(myMatch)
    return maxLengthOf

assert paran("((((())(((()") == 4 #"(())"
assert paran("(((((") == 0
assert paran("()()()") == 6
assert paran("")  == 0
assert paran("((())()())()") == 12
assert paran("()()()((()()()()") == 8
assert paran("()()()()((()()())))()") == 18
assert paran("())))()()())))((()()())))()") == 10
