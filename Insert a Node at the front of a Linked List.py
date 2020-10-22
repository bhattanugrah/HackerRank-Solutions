#Problem Link: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem

def insertNodeAtHead(llist, data):
    temp = SinglyLinkedNode(data)
    temp.next = llist
    return temp
