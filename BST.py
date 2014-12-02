class Node:
    def __init__(self, number):
        self._number = number
        self._father = None
        self._left = None
        self._right = None
    
    def setNumber(self, number):
        self._number = number
    
    def setFather(self, father):
        self._father = father
    
    def setLeft(self, left):
        self._left = left
    
    def setRight(self, right):
        self._right = right

    def getNumber(self):
        return self._number
    
    def getFather(self):
        return self._father
    
    def getLeft(self):
        return self._left
    
    def getRight(self):
        return self._right

class BinarySearchTree:
    def __init__(self):
        self._root = None
    
    def setRoot(self, newRoot):
        self._root = newRoot
    
    def getRoot(self):
        return self._root
    
    def empty_tree(self):
        return self.getRoot is None
    
    def pre_order(self, nodeWalker, arr2return = []):
        if self.empty_tree():
            return 0
        
        if nodeWalker is not None:
            arr2return.append(str(nodeWalker.getNumber()))
            self.pre_order(nodeWalker.getLeft(), arr2return)
            self.pre_order(nodeWalker.getRight(), arr2return)
        return arr2return
    
    def in_order(self, nodeWalker, arr2return = []):
        if self.empty_tree():
            return 0
        
        if nodeWalker is not None:
            self.in_order(nodeWalker.getLeft(), arr2return)
            arr2return.append(str(nodeWalker.getNumber()))
            self.in_order(nodeWalker.getRight(), arr2return)
        return arr2return
    
    def post_order(self, nodeWalker, arr2return = []):
        if self.empty_tree():
            return 0
        
        if nodeWalker is not None:
            self.post_order(nodeWalker.getLeft())
            self.post_order(nodeWalker.getRight())
            arr2return.append(str(nodeWalker.getNumber()))
        return arr2return
    
    def minimum(self,nodeWalker):
        while nodeWalker.getLeft() is not None:
            nodeWalker = nodeWalker.getLeft()
        return nodeWalker
    
    def maximum(self, nodeWalker):
        while nodeWalker.getRight() is not None:
            nodeWalker = nodeWalker.getRight()
        return nodeWalker
    
    def successor(self, xNode):
        if xNode.getRight() is not None:
            return self.minimum(xNode.getRight())
        
        if xNode.getFather() is not None:
            yNode = xNode.getFather()
            while ((yNode is not None) and
                   (xNode is yNode.getFather())):
                xNode = yNode
                yNode = yNode.getFather()
        
        else:
            return None
        
        return yNode
    
    def predecessor(self, xNode):
        if xNode.getLeft() is not None:
            return self.maximum(xNode.getLeft())
        
        if xNode.getFather() is not None:
            yNode = xNode.getFather()
            while ((yNode is not None) and
                   (xNode is yNode.getFather())):
                xNode = yNode
                yNode = yNode.getFather()
        
        else:
            return None
        
        return yNode
    
    def node_insert(self, node2ins):
        yNode = None
        xNode = self.getRoot()
        while xNode is not None:
            yNode = xNode
            if node2ins.getNumber() < xNode.getNumber():
                xNode = xNode.getLeft()
            else:
                xNode = xNode.getRight()
        
        node2ins.setFather(yNode)
        if yNode is None:
            self.setRoot(node2ins)
        else:
            if node2ins.getNumber() < yNode.getNumber():
                yNode.setLeft(node2ins)
            else:
                yNode.setRight(node2ins)
    
    def node_remove(self, node2rem):
        if ((node2rem.getLeft() is None) or
            (node2rem.getRight() is None)):
            yNode = node2rem
        else:
            yNode = self.successor(node2rem)
        
        if yNode.getLeft() is not None:
            xNode = yNode.getLeft()
        else:
            xNode = yNode.getRight()
        
        if xNode is not None:
            xNode.setFather(yNode.getFather())
        
        if yNode.getFather() is None:
            self.setRoot(xNode)
        else:
            if yNode is yNode.getFather().getLeft():
                yNode.getFather().setLeft(xNode)
            else:
                yNode.getFather().setRight(xNode)
        
        if yNode is not node2rem:
            node2rem.setNumber(yNode.getNumber())
        
        return yNode
