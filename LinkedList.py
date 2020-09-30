# Node Class implenetation
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Linked List implementation
class LinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.length = 0
        if (lst is not None):
            for elem in lst: self.append(elem)

    def __len__(self):
        return self.length

    def __str__(self):
        listStr = '[ '
        currentNode = self.head
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
        currentNode, currentKey = self.head, 0
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
        currentNode, currentKey = self.head, 0
        while currentNode is not None:
            if (currentKey == key): currentNode.data = value
            currentNode = currentNode.next
            currentKey += 1
    
    # Private method to check whether the key is out of List range
    def __checkIndex(self, key):
        if (key >= self.length): 
            raise IndexError('LinkedList index out of range')

    def append(self, data):
        if (self.head is None):
            self.head = Node(data)
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = Node(data)
        self.length += 1

    def pop(self, key = None):
        if (key == 0):
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return

        if (key is None): key = len(self)-1
        self.__checkIndex(key)

        currentNode, currentInd = self.head, 0
        prevNode = None
        while currentNode is not Node():
            if (currentInd == key): 
                prevNode.next = currentNode.next
                currentNode.next = None
                self.length -= 1
                return
            prevNode = currentNode
            currentNode = currentNode.next
            currentInd += 1

    def reverse(self):
        currentNode = self.head
        temp = []
        while currentNode is not None:
            temp.append(currentNode.data)
            currentNode = currentNode.next

        currentNode = self.head
        for elem in reversed(temp):
            currentNode.data = elem
            currentNode = currentNode.next

    def copy(self):
        copy = LinkedList()
        currentNode = self.head
        while currentNode is not None:
            copy.append(currentNode.data)
            currentNode = currentNode.next

        return copy

    def print(self):
        print(str(self))