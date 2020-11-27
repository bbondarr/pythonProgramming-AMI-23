from strategies.Strategy import Strategy
from LinkedList import LinkedList

class Validation:
    def __init__(self): 
        pass

    @staticmethod
    def validatePositiveInt(val, _str):
        try:
            val = int(val)
            if val < 0:
                raise ValueError(_str+' must be a positive integer')
        except ValueError: 
            raise ValueError(_str+' must have an integer value')
        
        return val        

    @staticmethod
    def validateFileName(val, _str='Filename'):
        if not isinstance(val, str):
            raise ValueError(_str+' must have a string value')        
        if  not val.endswith('.txt'):
            raise ValueError(_str+' must be txt format')

        return val

    @staticmethod
    def validateIndex(val, lst, _str='Insertion position'):
        if val > len(lst):
            raise IndexError(_str+' out of range')

    @staticmethod
    def validateLinkedList(func):
        def inner(_self, val):
            if not isinstance(val, LinkedList):
                raise ValueError('Value must be of type LinkedList')
            func(_self, val)

        return inner

    @staticmethod
    def validateStrategy(func):  
        def inner(_self, val):
            if not isinstance(val, Strategy):
                raise ValueError('Value must be a Strategy subclass') 
            func(_self, val)

        return inner