from BST import *

numArray = [4, 2, 6, 1, 3, 5, 7]

print("numArray:", numArray)

##Binary Tree pseudo-random key allocation
tree = BinarySearchTree()
for i in range(7):
    tree.node_insert(Node(numArray[i]))

##pre-order walk
print("\nPre-order walk:")
print(tree.pre_order(tree.getRoot()))

##in-order walk
print("\nIn-order walk:")
print(tree.in_order(tree.getRoot()))

##pos-order walk
print("\nPos-order walk:")
print(tree.post_order(tree.getRoot()))
