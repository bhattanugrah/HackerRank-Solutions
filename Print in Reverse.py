#Problem Link: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

def reversePrint(head):
    if head is None:
        return None
    else:
        stack=[]
        while head:
            stack.append(head.data)
            head = head.next
        while stack:
            print(stack.pop())
