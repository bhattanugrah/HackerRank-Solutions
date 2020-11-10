#Problem Link: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_r=next-challenge&h_v=zen

def sortedInser(head, data):
    node = DoublyLinkedListNode(data)
    if head == None:
        head = node
    elif data<head.data:
        node.next = head
        head.prev = node
        head = node

    else:
        cur = head
        while cur.next != None and cur.data < data:
            cur = cur.next
        if cur.next == None and cur.data < data:
            cur.next = node
            node.prev = cur
        else:
            previous = cur.prev
            previous.next = node
            node.prev = previous
            node.next = cur
            cur.prev = node
    return head