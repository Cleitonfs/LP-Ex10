from BST import *
import sys

try:
    fileIN = open(sys.argv[1], 'r')
except IndexError:
    fileIN = open("E10IN.txt", 'r')

while True:
    numCases = int(fileIN.readline())
    binTree = BinarySearchTree()
    
    for case in range(numCases):
        fLine = fileIN.readline().split()
        if fLine[0] == 'A':
            binTree.node_insert(Node(fLine[1]))
        
        elif fLine[0] == 'B':
            binTree.node_remove(Node(fLine[1]))
        
        elif fLine[0] == 'C':
            print(binTree.predecessor(tree.getRoot()))
        
        elif fLine[0] == "PRE":
            print(' 'join.(binTree.pre_order(binTree.getRoot())))
        
        elif fLine[0] == "IN":
            print(' 'join.(binTree.in_order(binTree.getRoot())))
        
        elif fLine[0] == "POST":
            print(' 'join.(binTree.post_order(binTree.getRoot())))
    ##TO-DO:
    ##outer loop check
    ##Output File write

fileIN.close()
