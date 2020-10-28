#Problem Link: https://www.hackerrank.com/challenges/largest-rectangle/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def largestRectangle(h):
    stack = []
    area = i = 0
    h.append(0)

    #Main Logic
    while i<len(h):
        #stack is empty or greater height is found
        if not stack or h[stack[-1]] < h[i]:
            #push the index of the building
            stack.append(i)
            i += 1

        #if height is lesser
        else:
            top = stack.pop()
            area = max(area, h[top]*(i-stack[-1]-1 if stack else i))

    return area