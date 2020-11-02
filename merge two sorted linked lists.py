#Problem Link: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

def mergeLists(head1, head2):
    if (head1 is None):
        return head2
    elif (head2 is None):
        return head1

    if (head1.data <= head2.data):
        result = head1
        result.next = mergeLists(head1.next, head2)
    else:
        result = head2
        result.next = mergeLists(head1, head2.next)

    return result
