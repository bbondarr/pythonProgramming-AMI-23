# Node Class implenetation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List implementation
class LinkedList:
    def __init__(self, lst=None):
        self.__head = None
        self.__length = 0
        if (lst is not None):
            for elem in lst: self.append(elem)

    def __len__(self):
        return self.__length

    def __str__(self):
        listStr = '[ '
        currentNode = self.__head
        while currentNode is not None:
            listStr += str(currentNode.data)+' '
            currentNode = currentNode.next
        return listStr + ']'

    # getitem + getslice implementation
    def __getitem__(self, key):
        #getslice
        if (isinstance(key, slice)):
            begin, end, step = key.indices(len(self))
            self.__checkIndex(begin)

            subList = LinkedList()
            for i in range(begin, end, step):
                subList.append(self[i])
            return subList

        self.__checkIndex(key)
        currentNode, currentKey = self.__head, 0
        while currentNode is not None:
            if (currentKey == key): return currentNode.data
            currentNode = currentNode.next
            currentKey += 1

    # setitem + setslice implementation
    def __setitem__(self, key, value):
        # setslice
        if (isinstance(key, slice)):
            begin, end, step = key.indices(len(self))
            self.__checkIndex(begin)

            if (isinstance(value, (LinkedList, list))):
                j = 0
                for i in range(begin, end, step):
                    self[i] = value[j]
                    j += 1
            else: 
                for i in range(begin, end, step): 
                    self[i] = value
            return   

        self.__checkIndex(key)
        currentNode, currentKey = self.__head, 0
        while currentNode is not None:
            if (currentKey == key): currentNode.data = value
            currentNode = currentNode.next
            currentKey += 1
    
    # Private method to check whether the key is out of List range
    def __checkIndex(self, key):
        if (key >= self.__length): 
            raise IndexError('LinkedList index out of range')

    def append(self, data):
        if (self.__head is None):
            self.__head = Node(data)
        else:
            currentNode = self.__head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = Node(data)
        self.__length += 1

    def insert(self, key, data):
        if (key == 0):
            newNode = Node(data)
            temp = self.__head
            self.__head = newNode
            newNode.next = temp
            self.__length += 1
            return

        self.__checkIndex(key)

        currentNode, currentInd = self.__head, 0
        prevNode = None
        while currentNode is not None:
            if (currentInd == key): 
                newNode = Node(data) 
                prevNode.next = newNode
                newNode.next = currentNode
                self.__length += 1
                return
            prevNode = currentNode
            currentNode = currentNode.next
            currentInd += 1

    def pop(self, key = None):
        if (key == 0):
            temp = self.__head
            self.__head = self.__head.next
            temp.next = None
            self.__length -= 1
            return

        if (key is None): key = len(self)-1
        self.__checkIndex(key)

        currentNode, currentInd = self.__head, 0
        prevNode = None
        while currentNode is not None:
            if (currentInd == key): 
                prevNode.next = currentNode.next
                currentNode.next = None
                self.__length -= 1
                return
            prevNode = currentNode
            currentNode = currentNode.next
            currentInd += 1

    def reverse(self):
        currentNode = self.__head
        temp = []
        while currentNode is not None:
            temp.append(currentNode.data)
            currentNode = currentNode.next

        currentNode = self.__head
        for elem in reversed(temp):
            currentNode.data = elem
            currentNode = currentNode.next

    def copy(self):
        copy = LinkedList()
        currentNode = self.__head
        while currentNode is not None:
            copy.append(currentNode.data)
            currentNode = currentNode.next

        return copy

    def clear(self): 
        for i in range(self.__length):
            self.pop(0)