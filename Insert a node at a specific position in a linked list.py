#Problem Link: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    if position == 0:
        node.next = head
        head = node
        return head
    temp = head
    c = 1
    while temp.next != None:
        if c == position:
            node.next = temp.next
            temp.next = node
            break
        c+=1
        temp=temp.next
    return head