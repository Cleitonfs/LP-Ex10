class Node:
    def __init__(self, key, data):
        self._key = key
        self._data = data
        self._father = None
        self._left = None
        self._right = None
    
    def setKey(self, key):
        self._key = key
    
    def setData(self, data):
        self._data = data
    
    def setFather(self, father):
        self._father = father
    
    def setLeft(self, left):
        self._left = left
    
    def setRight(self, right):
        self._right = right

    def getKey(self):
        return self._key
    
    def getData(self):
        return self._data
    
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
    
    def pre_order(self, nodeWalker):
        if nodeWalker is not None:
            print("Node:", nodeWalker.getData())
            self.pre_order(nodeWalker.getLeft())
            self.pre_order(nodeWalker.getRight())
    
    def in_order(self, nodeWalker):
        if nodeWalker is not None:
            self.in_order(nodeWalker.getLeft())
            print("Node:", nodeWalker.getData())
            self.in_order(nodeWalker.getRight())
    
    def pos_order(self, nodeWalker):
        if nodeWalker is not None:
            self.pos_order(nodeWalker.getLeft())
            self.pos_order(nodeWalker.getRight())
            print("Node:", nodeWalker.getData())
    
    def search(self, nodeWalker, key):
        if ((nodeWalker is none) or (key == nodeWalker.getKey())):
            return nodeWalker
        
        if key < nodeWalker.getKey():
            return self.search(nodeWalker.getLeft(), key)
        else:
            return self.search(nodeWalker.getRight(), key)
    
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
            if node2ins.getKey() < xNode.getKey():
                xNode = xNode.getLeft()
            else:
                xNode = xNode.getRight()
        
        node2ins.setFather(yNode)
        if yNode is None:
            self.setRoot(node2ins)
        else:
            if node2ins.getKey() < yNode.getKey():
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
            node2rem.setKey(yNode.getKey())
            node2rem.setData(yNode.getData())
        
        return yNode
