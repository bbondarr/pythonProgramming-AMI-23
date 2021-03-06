class MersennePrimesIterator:
    def __init__(self, N):
        self._pow = 1
        self.mersenne = 3
        self.N = N
        self.counter = 0

    def __iter__(self): 
        return self

    def __next__(self):
        if self.counter >= self.N:
            raise StopIteration

        while (self.counter < self.N):
            self._pow += 1
            self.mersenne = 2**self._pow - 1 
            if (self.__isMersennePrime()): 
                self.counter += 1
                return self.mersenne

    def __isMersennePrime(self):
        if self._pow == 2: return True

        S = 4
        i = 1
        while (i != self._pow - 1):
            S = (S*S - 2) % self.mersenne
            i += 1
            
        return S == 0           