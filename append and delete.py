#Problem Link: https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s, t, k):
    count = 0

    for i, j in zip (s, t):
        if i == j:
            count+=1
        else:
            break

    total_length = len(s) + len(t)

    if total_length <= 2*count+k and total_length%2 == k%2 or total_length<k:
        return "Yes"
    else:
        return "No"
