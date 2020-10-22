#Problem Link: https://www.hackerrank.com/challenges/dynamic-array/problem

def dynamicArray(n, queries):
    seqList = [[] for i in range(n)]
    lastAnswer = 0
    result=[]
    for q in queries:
        if q[0]==1:
            seq=(q[1] ^ lastAnswer)%n
            seqList[seq].append(q[2])
        else:
            seq=(q[1] ^ lastAnswer)%n
            lastAnswer = seqList[seq][q[2]%len(seqList[seq])]
            result.append(lastAnswer)
    return result