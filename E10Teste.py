from TreeAndNode import *
import sys

try:
    fileIN = open(sys.argv[1], 'r')
except IndexError:
    fileIN = open("E10.in", 'r')

try:
    fileOUT = open(sys.argv[2], 'w')
except IndexError:
    fileOUT = open("E10.out", 'w')

caseCounter = 1

while True:
    numCases = fileIN.readline()
    
    if numCases == '': #EOF check
        break

    fileOUT.write("Caso " + str(caseCounter) + ":\n")
    tree = BinarySearchTree()
    
    for case in range(int(numCases)):
        fLine = fileIN.readline().split()
        
        if fLine[0] == 'A':
            tree.node_insert(Node(fLine[1]))
        
        elif fLine[0] == 'B':
            node2Bdel = tree.search(tree.getRoot(), fLine[1])
            tree.node_remove(node2Bdel)
        
        elif fLine[0] == 'C':            
            if((tree.is_empty()) or
               (tree.getRoot().getLeft() is None) and
               (tree.getRoot().getLeft() is None)):
                fileOUT.write("0\n")
            
            else:
                nodePivot = tree.search(tree.getRoot(), fLine[1])
                tooBigOfALine = str(tree.predecessor_alt(nodePivot).getValue())
                fileOUT.write(tooBigOfALine + '\n')
        
        elif fLine[0] == "PRE":
            if tree.is_empty() == True:
                fileOUT.write("0\n")
            else:
                fileOUT.write(tree.pre_order(tree.getRoot())[:-1] + '\n')
        
        elif fLine[0] == "IN":
            if tree.is_empty() == True:
                fileOUT.write("0\n")
            else:
                fileOUT.write(tree.in_order(tree.getRoot())[:-1] + '\n')
        
        
        elif fLine[0] == "POST":
            if tree.is_empty() == True:
                fileOUT.write("0\n")
            else:
                fileOUT.write(tree.post_order(tree.getRoot())[:-1] + '\n')

    caseCounter += 1

fileIN.close()
fileOUT.close()
