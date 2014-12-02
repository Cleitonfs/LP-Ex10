from _BinarySearchTree import *

keyArray = [4, 2, 6, 1, 3, 5, 7]
dataArray = ["d4", "d2", "d6", "d1", "d3", "d5", "d7"]

print("keyArray:", keyArray)
print("dataArray:", dataArray)

##Binary Tree pseudo-random key allocation
tree = BinarySearchTree()
for i in range(7):
    tree.node_insert(Node(keyArray[i],dataArray[i]))

##pre-order walk
print("\nPre-order walk:")
tree.pre_order(tree.getRoot())

##in-order walk
print("\nIn-order walk:")
tree.in_order(tree.getRoot())

##pos-order walk
print("\nPos-order walk:")
tree.pos_order(tree.getRoot())
