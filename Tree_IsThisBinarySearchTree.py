#Problem Link: https://www.hackerrank.com/challenges/is-binary-search-tree/problem

def inOrder(root, tree):
    if root is None:
        return
    else:
        inOrder(root.left, tree)
        tree.append(root.data, tree)
        inOrder(tree.right, tree)

def check_binary_search_tree(root):
    tree = []
    inOrder(root, tree)
    if tree==sorted(set(tree)):
        return True
    else:
        return False