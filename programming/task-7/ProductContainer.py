import json
from datetime import date
from Product import Product
from Validation import Validation as v
        
class ProductContainer: 

    class PC_Memento:
        def __init__(self, collection):
            self.listSnapshot = [p.copy() 
                for p in collection._ProductContainer__productList]


    def __init__(self, attachedJSON=None):
        self.__productList = []
        self.__fn = attachedJSON

    def __str__(self):
        productsStr = '[\n'
        for p in self.__productList:
            productsStr += str(p) + '\n'
        productsStr += ']'

        return productsStr

    def __len__(self):
        return len(self.__productList)

    def sort(self, attr='createdAt'):
        _attr = attr[0].upper() + attr[1:]
        _attr = 'get'+_attr
        lst = self.__productList

        try:
            if isinstance(getattr(lst[0], _attr)(), str):
                lst.sort(key=lambda p: getattr(p, _attr)().lower())
            else:
                lst.sort(key=lambda p: getattr(p, _attr)())

        except AttributeError: 
            raise AttributeError('\'Product\'object has no attribute \''+attr+'\'')

    def find(self, key):
            res = ProductContainer()
            key = str(key).lower()
            for p in self.__productList:
                for a in Product.getGetters():
                    if str(getattr(p, a)()).lower().find(key) != -1:
                        if p not in res._ProductContainer__productList: 
                            res.add(p)

            return res if len(res) != 1 else res._ProductContainer__productList[0]

    def delete(self, ID):
        i = -1
        for p in self.__productList:
            if p.getID() == ID: 
                self.__productList.pop(i); break        
        else: 
            raise NameError('No product with such ID found')
        
        if self.__fn: self.writeIntoFile(self.__fn)

    def add(self, product): 
        self.__productList.append(product)
        if self.__fn: self.writeIntoFile(self.__fn)

    def edit(self, ID, attr, val):
        _attr = attr[0].upper() + attr[1:]
        _attr = 'set'+_attr
        for p in self.__productList:
            if p.getID() == ID: 
                getattr(p, _attr)(val)
                break
        else: 
            raise NameError('No product with such ID found')
        
        if self.__fn: self.writeIntoFile(self.__fn)

    @v.validateStr
    @v.validateFileName
    def readFromFile(self, filename):        
        self.__productList = []
        with open(filename) as file:
            jsonLst = json.load(file)

        i = 0
        for _dict in jsonLst:
            i+=1
            try:
                p = Product(**{a:_dict.get(a) for a in Product.getAttributes()})
            except ValueError as ve:
                print('Product %d Error: ' % (i) + str(ve)); continue

            self.__productList.append(p)

    @v.validateStr
    @v.validateFileName
    def writeIntoFile(self, filename):     
        file = open(filename, mode='w')
        file.write('[')
        for p in self.__productList:
            file.write(p.toJSON())
            if p != self.__productList[len(self)-1]: 
                file.write(', ')
        file.write(']')
        file.close()

    # MEMENTO METHODS
    def save(self):
        return self.PC_Memento(self)

    def restore(self, memento):
        self.__productList = memento.listSnapshot.copy()
        if self.__fn: self.writeIntoFile(self.__fn)