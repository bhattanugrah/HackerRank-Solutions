#Problem Link: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

def mergeLists(head1, head2):
    if head1 is None and head2 is None:
        return None

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data < head2.data:
        smallerNode = head1.data
        smallerNode.next = mergeLists(head1.next, head2)
    else:
        smallerNode = head2.data
        smallerNode.next = mergeLists(head1, head2.next)