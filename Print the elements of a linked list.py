#Problem Link: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

def printLinkedList(head):
    while (head):
        print(head.data)
        head = head.next
