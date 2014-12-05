from TreeAndNode import *

tr = BinarySearchTree()

numArray = [4, 2, 6, 1, 3, 5, 7]

print("numArray:", numArray)

##Binary Tree pseudo-random key allocation
tree = BinarySearchTree()
for i in range(7):
    tree.node_insert(Node(numArray[i]))

a = tree.traversal("PRE")
b = tree.traversal("IN")
c = tree.traversal("POST")
print("a:", a)
print("b:", b)
print("c:", c)

#print("PRE:")
#tree.traversal("PRE")

#print("IN:")
#tree.traversal("IN")

#print("POST:")
#tree.traversal("POST")

t = BinarySearchTree()
#print(t.predecessor(t.getRoot()))

nodeP = tree.search(tree.getRoot(), 5)
print(nodeP.getValue())
#t.node_insert(Node(3))
#print(t.predecessor(t.getRoot()))

tree = BinarySearchTree()
tree.node_insert(Node(5))
tree.node_insert(Node(6))
tree.node_insert(Node(6))
tree.node_insert(Node(6))
tree.node_insert(Node(6))
tree.node_insert(Node(1))

searc = tree.search(tree.getRoot(), 6)
print("Pred:", tree.predecessor(searc).getValue())
print("Pred_alt:", tree.predecessor_alt(searc).getValue())

print("in:", tree.in_order(tree.getRoot()))
nodeP = tree.search(tree.getRoot(), 6)
print ("nodeP.getValue():", nodeP.getValue())
tree.node_remove(nodeP)
print("tree.getRoot():", tree.getRoot())
print("in:", tree.in_order(tree.getRoot()))

nodeP = tree.search(tree.getRoot(), 6)
print ("nodeP.getValue():", nodeP.getValue())
tree.node_remove(nodeP)
print("tree.getRoot():", tree.getRoot())
print("in:", tree.in_order(tree.getRoot()))
nodeP = tree.search(tree.getRoot(), 6)
print ("nodeP.getValue():", nodeP.getValue())
tree.node_remove(nodeP)
print("tree.getRoot():", tree.getRoot())
print("in:", tree.in_order(tree.getRoot()))


