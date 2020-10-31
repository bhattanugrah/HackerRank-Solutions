#Problem Link: https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

def compare_list(list1, llist2):
    p1 = llist1
    p2 = llist2
    flag = True
    while p1!=None and p2!=None:
        if p1.data == p2.data:
            p1 = p1.next
            p2 = p2.next
            continue
        flag = False
        break
    if (p1!=None and p2==None) or (p1==None and p2!=None):
        flag = False
    if flag:
        return 1
    return 0