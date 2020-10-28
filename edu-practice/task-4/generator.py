def isMersennePrime(mersenne, _pow):
    if _pow == 2: return True

    S = 4
    i = 1
    while (i != _pow - 1):
        S = (S*S - 2) % mersenne
        i += 1
        
    return S == 0

def MersennePrimesGenerator(n):
    _pow = 2
    mersenne = 3
    i = 0
    while (i < n):
        if (isMersennePrime(mersenne, _pow)): 
            yield mersenne
            i += 1
        _pow += 1
        mersenne = 2**_pow - 1