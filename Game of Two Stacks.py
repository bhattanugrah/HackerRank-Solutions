#Problem Link: https://www.hackerrank.com/challenges/game-of-two-stacks/problem?isFullScreen=true

def twoStacks(x, a, b):
    maxnum = total = i = j = 0:
    while i<len(a) and total + a[i] <= x:
        total += a[i]
        i += 1
        maxnum += 1
    while j<len(b) and i>0:
        total += b[j]
        j += 1
        while i>0 and total>x:
            i -= 1
            total -= a[i]
        if total <= x and maxnum<i+j:
            maxnum = i+j
    return maxnum
