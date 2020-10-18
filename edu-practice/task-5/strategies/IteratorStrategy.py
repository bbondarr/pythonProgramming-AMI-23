import random
from strategies.Strategy import Strategy

class IteratorStrategy(Strategy):
    def __init__(self):
        pass

    def execute(self, lst, pos, N):
        _iter = self.MersennePrimesIterator(N)
        for i in _iter:
            lst.insert(pos+_iter.i-1, i)
            print(lst, len(lst))
        return lst

    def getName(self):
        return 'iterator'  

    class MersennePrimesIterator:
        def __init__(self, N):
            self._pow = 1
            self.mersenne = 3
            self.N = N
            self.i = 0

        def __iter__(self): 
            return self

        def __next__(self):
            if self.i >= self.N:
                raise StopIteration

            while (self.i < self.N):
                self._pow += 1
                self.mersenne = 2**self._pow - 1 
                if (self.__isMersennePrime()): 
                    self.i += 1
                    return self.mersenne

        def __isMersennePrime(self):
            if self._pow == 2: return True

            S = 4
            i = 1
            while (i != self._pow - 1):
                S = (S*S - 2) % self.mersenne
                i += 1
                    
            return S == 0        