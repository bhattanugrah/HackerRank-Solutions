#Problem Link: https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

def findMergeNode(head1, head2):
    def getcount(head):
        n = 0
        while head.next != None:
            head = head.next
            n += 1
        return n

    def getnode(d, head1, head2):
        for i in range(d):
            head1 = head1.next

        while head1 and head2:
            if head1 == head2:
                return head1.data
            else:
                head1 = head1.next
                head2 = head2.next

    c1 = getcount(head1)
    c2 = getcount(head2)

    if c1>c2:
        return (c1-c2, head1, head2)
    else:
        return (c2-c1, head2, head1)

