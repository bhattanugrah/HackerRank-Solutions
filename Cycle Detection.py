#Problem link: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

def has_cycle(head):
    traversed=[]
    while head!=None:
        if head in traversed:
            return 1
        else:
            traversed.append(head)
            head=head.next
    return 0

