#problem Link: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

def height(root):
    if root==None:
        return -1
    else:
        return max(height(root.left), height(root.right))+1