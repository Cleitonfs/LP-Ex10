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
        print("EOF!")
        break

    print("Caso " + str(caseCounter) + ':')
    fileOUT.write("Caso " + str(caseCounter) + ":\n")

    tree = BinarySearchTree()
    
    for case in range(int(numCases)):
#        print("case:", str(case + 1))
#        print("tree.getRoot():", tree.getRoot())
        
        fLine = fileIN.readline().split()
#        print("linha:", fLine)
        
        if fLine[0] == 'A':
            tree.node_insert(Node(fLine[1]))
        
        elif fLine[0] == 'B':
            node2Bdel = tree.search(tree.getRoot(), fLine[1])
            tree.node_remove(node2Bdel)
        
        elif fLine[0] == 'C':
            if tree.is_empty() == True:
                print(0)
                fileOUT.write("0\n")
            
            elif (tree.getRoot().getLeft() is None and
                  tree.getRoot().getLeft() is None):
                print(0)
                fileOUT.write("0\n")
            
            else:
                nodePivot = tree.search(tree.getRoot(), fLine[1])
                print(tree.predecessor_alt(nodePivot).getValue())
                fileOUT.write(str(tree.predecessor_alt(nodePivot).getValue()) + '\n')
        
        elif fLine[0] == "PRE":
            if tree.is_empty() == True:
                print("PRE:", '0')
                fileOUT.write("0\n")
            else:
                print("PRE:", tree.pre_order(tree.getRoot()))
                fileOUT.write(tree.pre_order(tree.getRoot())[:-1] + '\n')
        
        elif fLine[0] == "IN":
            if tree.is_empty() == True:
                print("IN:", '0')
                fileOUT.write("0\n")
            else:
                print("IN:", tree.in_order(tree.getRoot()))
                fileOUT.write(tree.in_order(tree.getRoot())[:-1] + '\n')
        
        
        elif fLine[0] == "POST":
            if tree.is_empty() == True:
                print("POST:", '0')
                fileOUT.write("0\n")
            else:
                print("POST:", tree.post_order(tree.getRoot()))
                fileOUT.write(tree.post_order(tree.getRoot())[:-1] + '\n')
        

#        print("IN_DEBUG:", tree.traversal("IN"))
    caseCounter += 1
    
    
##TO-DO:
##Remover depuracao das cavernas

fileIN.close()
fileOUT.close()
