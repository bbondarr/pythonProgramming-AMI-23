from Validation import Validation as v
from LinkedList import LinkedList

class Context:
    def __init__(self):
        self.__lst = LinkedList()
        self.__strategy = None

    def setStrategy(self, strategy):        
        self.__strategy = v.validateStrategy(strategy)

    def strategy(self):
        return self.__strategy.getName() if self.__strategy else None

    def lst(self):
        return self.__lst

    def executeStrategy(self, *args):
        if self.__strategy is not None:
            self.__lst = self.__strategy.execute(self.__lst, *args)