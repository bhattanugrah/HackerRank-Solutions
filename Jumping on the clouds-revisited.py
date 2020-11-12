#problem Link: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

def jumpingOnClouds(c, k):
    energy = 100
    i = 0
    n = len(c)

    while True:
        i = (i+k)%n
        if c[i] == 1:
            energy = energy - 3
        else:
            energy = energy - 1

        if i == 0:
            break
    return energy

