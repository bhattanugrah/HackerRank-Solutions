#Problem Link: https://www.hackerrank.com/challenges/equal-stacks/problem

def equalStacks(h1, h2, h3):
    h1=h1[::-1]
    h2=h2[::-1]
    h3=h3[::-1]

    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    while True:
        minheight = min(sum1, sum2, sum3)

        if minheight == 0:
            return 0

        if minheight < sum1:
            sum1 -= h1.pop()
        if minheight < sum2:
            sum2 -= h2.pop()
        if minheight < sum3:
            sum3 -= h3.pop()

        if sum1 == sum2 == sum3:
            return sum1
