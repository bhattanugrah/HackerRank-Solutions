#Problem Link: https://www.hackerrank.com/challenges/arrays-ds/problem

def reverseArray(a):
    rev_arr = []
    n=len(a)
    for i in range(n-1, -1, -1):
        rev_arr.append(a[i])
    return rev_arr





