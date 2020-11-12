#Link to Problem: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

def reverse(head):
    head.prev, head.next = head.next, head.prev
    if head.prev != None:
        return reverse(head.prev)
    else:
        return head
