import random
from strategies.Strategy import Strategy
from strategies.MersennePrimesIterator import MersennePrimesIterator

class IteratorStrategy(Strategy):
    def __init__(self):
        pass

    def execute(self, lst, pos, N):
        _iter = MersennePrimesIterator(N)
        for i in _iter:
            lst.insert(pos+_iter.i-1, i)

        return lst

    def getName(self):
        return 'iterator'          