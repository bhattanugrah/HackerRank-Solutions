#Problem Link: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem?h_r=next-challenge&h_v=zen

def reverse(head):
    p1 = head
    p2 = p1.next
    p3 = p2.next
    p1.next = None
    while p3 is not None:
        p1 = p2
        p2 = p3
        p3 = p3.next
        p2.next = p1
    return p2

