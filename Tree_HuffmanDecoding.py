#Problem Link: https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

def decodeHuff(root, s):
    temp = root
    decoded = []

    for char in s:
        if char is '0':
            temp = temp.left
        else:
            temp = temp.right

        if temp.left is None and temp.right is None:
            decoded.append(temp.data)
            temp=root

    print("".join(decoded))
    