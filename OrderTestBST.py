from BST import *

##numArray = [4, 2, 6, 1, 3, 5, 7]
##
##print("numArray:", numArray)
##
####Binary Tree pseudo-random key allocation
##tree = BinarySearchTree()
##for i in range(7):
##    tree.node_insert(Node(numArray[i]))
##
####pre-order walk
##print("\nPre-order walk:")
##print(tree.pre_order(tree.getRoot()))
##
####in-order walk
##print("\nIn-order walk:")
##print(tree.in_order(tree.getRoot()))
##
####pos-order walk
##print("\nPos-order walk:")
##print(tree.post_order(tree.getRoot()))
##
##print()
##print("tree.search(tree.getroot(), 2)", tree.predecessor(tree.search(tree.getRoot(), 2)).getNumber())

fIN = open("E10IN.txt", 'r')
fIN.readline()

oO = BinarySearchTree()
print(oO.in_order(oO.getRoot()))

for i in range(5):
    linha = fIN.readline().split()
    print(int(linha[1]))
    oO.node_insert(Node(int(linha[1])))
##    print(oO.in_order(oO.getRoot()))

print("\n1:", oO.in_order(oO.getRoot()))
##print("\n2:", oO.in_order(oO.getRoot()))
##print("\n3:", oO.in_order(oO.getRoot()))
