#Problem Link: https://www.hackerrank.com/challenges/array-left-rotation/problem

def rotateLeft(d, arr):
    return arr[d:] + arr[:d]