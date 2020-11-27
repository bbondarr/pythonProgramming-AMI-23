from abc import ABC, abstractmethod

class Strategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def execute(self, *args):
        pass