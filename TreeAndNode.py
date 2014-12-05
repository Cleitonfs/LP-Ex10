class Node:
    """Define os nodos individuais para estruturas encadeadas

    Atributos:
        _value (obj): valor a ser armazenado
        _father (ponteiro): endereco do no pai, inicializado com None
        _left (ponteiro): endereco do filho esquerdo, inicio com None
        _right (ponteiro): endereco do filho direito, inicio com None
    """
    def __init__(self, value):
        self._value = value
        self._father = None
        self._left = None
        self._right = None
    
    def setValue(self, newValue):
        """Sobreescreve o atributo '_value' com um novo valor
        
        Argumentos:
            newValue (obj): novo valor a ser atribuido a '_valor'
        """
        self._value = newValue
    
    def setFather(self, newFather):
        """Sobreescreve o endereco do nodo pai com um novo valor
        
        Argumentos:
            newFather (obj): novo endereco para o nodo pai
        """
        self._father = newFather
    
    def setLeft(self, newLeft):
        """Sobreescreve a referencia para o nodo filho esquerdo com um
        novo endereco
        
        Argumentos:
            newLeft (obj): novo endereco para o nodo esquerdo
        """
        self._left = newLeft
    
    def setRight(self, newRight):
        """Sobreescreve a referencia para o nodo filho direito com um
        novo endereco
        
        Argumentos:
            newRight (obj): novo endereco para o nodo right
        """
        self._right = newRight

    def getValue(self):
        """Retorna o atributo '_value' armazenado no atual nodo
        
        Retorna:
            Objeto armazenado no atributo '_value' do objeto 'Nodo'
        """
        return self._value
    
    def getFather(self):
        """Retorna o endereco para o nodo pai do atual nodo
        
        Retorna:
            Referencia ao objeto 'Nodo' pai
        """
        return self._father
    
    def getLeft(self):
        """Retorna o endereco para o nodo filho esquerdo do atual nodo
        
        Retorna:
            Referencia ao objeto 'Nodo' filho esquerdo
        """
        return self._left
    
    def getRight(self):
        """Retorna o endereco para o nodo filho direito do atual nodo
        
        Retorna:
            Referencia ao objeto 'Nodo' filho direito
        """
        return self._right

class BinarySearchTree:
    """Define os metodos e o encadeamento de nodos em uma estrutura
    arvore de busca binaria

    Atributos:
        _root (obj): Armazena o nodo raiz da arvore
    """
    def __init__(self):
        self._root = None
    
    def setRoot(self, newRoot):
        """Sobreescreve o nodo raiz com um novo nodo
        
        Argumentos:
        newRoot (Node obj): Novo nodo a ser armazenado no atributo _root
        """
        self._root = newRoot
    
    def getRoot(self):
        """Retorna o objeto Nodo armazenado na raiz da arvore
        
        Retorna:
            Referencia ao objeto 'Nodo' raiz
        """
        return self._root
    
    def is_empty(self):
        """Verifica se a arvore se encontra vazia
        
        Retorna:
            Booleano, True se a lista esta vazia, False caso contrario
        """
        return self.getRoot() is None
    
    def pre_order(self, nodeWalker, str2ret = ''):
        """Metodo para travessia da arvore, modo pre-ordem
        
        Argumentos:
            nodeWalker (Node obj): Objeto Nodo que percorre a arvore
            str2ret (str): Concatena os valores armazenados em cada
            um dos nodos da arvore
        """
        if self.is_empty() == True:
            return 0
        
        if nodeWalker is not None:
            str2ret += (str(nodeWalker.getValue()) + ' ')
            str2ret = self.pre_order(nodeWalker.getLeft(), str2ret)
            str2ret = self.pre_order(nodeWalker.getRight(), str2ret)
            
        return str2ret
    
    def in_order(self, nodeWalker, str2ret = ''):
        """Metodo para travessia da arvore, modo em-ordem
        
        Argumentos:
            nodeWalker (Node obj): Objeto Nodo que percorre a arvore
            str2ret (str): Concatena os valores armazenados em cada
            um dos nodos da arvore
        """
        if self.is_empty() == True:
            return 0
        
        if nodeWalker is not None:
            str2ret = self.in_order(nodeWalker.getLeft(), str2ret)
#            print('.' + str(nodeWalker.getValue())) #CAVEMAN's DEBUG
            str2ret += (str(nodeWalker.getValue()) + ' ')
            str2ret = self.in_order(nodeWalker.getRight(), str2ret)
            
        return str2ret
    
    def post_order(self, nodeWalker, str2ret = ''):
        """Metodo para travessia da arvore, modo pos-ordem
        
        Argumentos:
            nodeWalker (Node obj): Objeto Nodo que percorre a arvore
            str2ret (str): Concatena os valores armazenados em cada
            um dos nodos da arvore
        """
        if self.is_empty() == True:
            return 0
        
        if nodeWalker is not None:
            str2ret = self.post_order(nodeWalker.getLeft(), str2ret)
#            print('.' + str(nodeWalker.getValue())) #CAVEMAN's DEBUG
            str2ret = self.post_order(nodeWalker.getRight(), str2ret)
            str2ret += (str(nodeWalker.getValue()) + ' ')
            
        return str2ret
    
    def traversal(self, traversalMode):
        """Controla o tipo de travessia da arvore e manipula o retorno
        da funcao recursiva de travessia
        
        Argumentos:
            traversalMode (str): String identificador do tipo de
            travessia
        
        Retorno:
            String contendo os valores armazenados em cada um dos nodos
        """
        if self.is_empty() == True:
            return 0
        
        array = []
        
        if traversalMode == "PRE":
            self.__pre_order(self.getRoot(), array)
        
        elif traversalMode == "POST":
            self.__post_order(self.getRoot(), array)
        
        else:
            self.__in_order(self.getRoot(), array)
        
        str2return = ' '.join(array)
        del array
        return str2return
    
    def __pre_order(self, nodeWalker, arr2return):
        """Metodo secundario para travessia da arvore, modo pre-ordem
        
        Argumentos:
            nodeWalker (Node obj): Objeto Nodo que percorre a arvore
            arr2return (array): Insere os valores armazenados em cada
            um dos nodos da arvore no array criado no escopo anterior
        """
        if nodeWalker is not None:
            arr2return.append(str(nodeWalker.getValue()))
            self.__pre_order(nodeWalker.getLeft(), arr2return)
            self.__pre_order(nodeWalker.getRight(), arr2return)
        return arr2return
    
    def __in_order(self, nodeWalker, arr2return = []):
        """Metodo secundario para travessia da arvore, modo em-ordem
        
        Argumentos:
            nodeWalker (Node obj): Objeto Nodo que percorre a arvore
            arr2return (array): Insere os valores armazenados em cada
            um dos nodos da arvore no array criado no escopo anterior
        """
        if nodeWalker is not None:
            self.__in_order(nodeWalker.getLeft(), arr2return)
            arr2return.append(str(nodeWalker.getValue()))
            self.__in_order(nodeWalker.getRight(), arr2return)
        return arr2return
    
    def __post_order(self, nodeWalker, arr2return):
        """Metodo secundario para travessia da arvore, modo pos-ordem
        
        Argumentos:
            nodeWalker (Node obj): Objeto Nodo que percorre a arvore
            arr2return (array): Insere os valores armazenados em cada
            um dos nodos da arvore no array criado no escopo anterior
        """
        if nodeWalker is not None:
            self.__post_order(nodeWalker.getLeft(), arr2return)
            self.__post_order(nodeWalker.getRight(), arr2return)
            arr2return.append(str(nodeWalker.getValue()))
        return arr2return
    
    def minimum(self,nodeWalker):
        """Percorre recursivamente a arvore em busca do nodo  om o menor
        valor armazenado, o nodo 'mais a esquerda'
        
        Argumentos:
            nodeWalker (Node obj): Objeto Nodo que percorre a arvore
        
        Retorno:
            Referencia ao objeto 'Nodo' com menor atributo '_valor'
            armazenado na arvore
        """
        while nodeWalker.getLeft() is not None:
            nodeWalker = nodeWalker.getLeft()
        return nodeWalker
    
    def maximum(self, nodeWalker):
        """Percorre recursivamente a arvore em busca do nodo com o maior
        valor armazenado, o nodo 'mais a direita'
        
        Argumentos:
            nodeWalker (Node obj): Objeto Nodo que percorre a arvore
        
        Retorno:
            Referencia ao objeto 'Nodo' com menor atributo '_valor'
            armazenado na arvore
        """
        while nodeWalker.getRight() is not None:
            nodeWalker = nodeWalker.getRight()
        return nodeWalker
    
    def search(self, nodeWalker, value):
        """Percorre recursivamente a arvore em busca do nodo contendo o
        valor 'value'
        
        Argumentos:
            nodeWalker (Node obj): Objeto Nodo que percorre a arvore
            value (int/str(int)): valor de comparacao para a ordenacao
            de nodos na arvore
        
        Retorno:
            Objeto Nodo armazenado na arvore com valor 'value'
        """
        if ((nodeWalker is None) or (value == nodeWalker.getValue())):
            return nodeWalker
        
        if value < nodeWalker.getValue():
            return self.search(nodeWalker.getLeft(), value)
        else:
            return self.search(nodeWalker.getRight(), value)
    
    def successor(self, xNode):
        """Percorre a arvore em busca do nodo com menor valor da
        sub-arvore direita do nodo 'xNode'
        
        Argumentos:
            xNode (Node obj): Nodo pivo
        
        Retorno:
            Referencia ao objeto Nodo sucessor de 'xNode'
        """
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
        """Percorre a arvore em busca do nodo com o maior valor da
        sub-arvore esquerda do nodo 'xNode'
        
        Argumentos:
            xNode (Node obj): Nodo pivo
        
        Retorno:
            Referencia ao objeto Nodo antecessor de 'xNode'
        """
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
    
    def predecessor_alt(self, nodePivot):
        xNode = nodePivot
        
        while xNode.getLeft() is not None:
            xNode = xNode.getLeft()
            if xNode.getValue() != nodePivot.getValue():
                return self.maximum(xNode.getLeft())
        
        xNode = nodePivot
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
        """Insere o objeto Nodo na arvore dependendo do seu atributo
        '_value'
        
        Argumentos:
            node2ins(Node obj): Objeto Nodo a ser inserido
        """
        yNode = None
        xNode = self.getRoot()
        while xNode is not None:
            yNode = xNode
            if node2ins.getValue() <= xNode.getValue():
                xNode = xNode.getLeft()
            else:
                xNode = xNode.getRight()
        
        node2ins.setFather(yNode)
        if yNode is None:
            self.setRoot(node2ins)
        else:
            if node2ins.getValue() <= yNode.getValue():
                yNode.setLeft(node2ins)
            else:
                yNode.setRight(node2ins)
    
    def node_remove(self, node2rem):
        """Remove o objeto Nodo referenciado da arvore e faz a
        manutencao de possiveis quebradas de referencia
        
        Atributos:
            node2rem (Node obj): Nodo a ser removido da arvore
        
        Retorno:
            Referencia ao objeto Nodo removido da arvore
        """
        if(node2rem.getLeft() is None) or (node2rem.getRight() is None):
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
            if yNode == yNode.getFather().getLeft():
                yNode.getFather().setLeft(xNode)
            else:
                yNode.getFather().setRight(xNode)
        
        if yNode != node2rem:
            node2rem.setValue(yNode.getValue)
        return yNode
