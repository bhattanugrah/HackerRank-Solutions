#Problem Link: https://www.hackerrank.com/challenges/sparse-arrays/problem

def matchingStrings(strings, queries):
    result=[]
    for i in range(len(queries)):
        counter=0
        for j in range(len(strings)):
            if queries[i]==strings[j]:
                counter +=1
        result.append(counter)
    return result
