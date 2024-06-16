# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true

def isValidParenthesis(s):
    stack = []
    hashmap = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for i in s:
        if i not in hashmap:
            stack.append(i)
        
        elif len(hashmap) == 0 or stack[-1] != hashmap[i]:
            return False
        
        else:
            stack.pop()

    return not stack

s = "()[]{}"
isValidParenthesis(s)
