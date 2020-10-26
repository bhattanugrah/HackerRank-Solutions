#Problem Link: https://www.hackerrank.com/challenges/balanced-brackets/problem

def isBalanced(s):
    stack = []
    brackets = {'{':'}', '(':')', '[':']'}

    for char in s:
        if char in ['{', '(', '[']:
            stack.append(char)
        else:
            if stack:
                top = stack.pop()
                if brackets[top] != char:
                    return 'NO'
            else:
                return "NO"
    return "NO" if stack else "Yes"