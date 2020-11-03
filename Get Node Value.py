#Problem Link: https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

def getNode(head, positionFromTail):
    ptr1 = head
    ptr2 = head

    if i in range(positionFromTail):
        ptr1 = ptr1.next

    while ptr1 != None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr2.data