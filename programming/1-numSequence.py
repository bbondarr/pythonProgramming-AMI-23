# Generate the sequence of Mersenne primes 

def isMersennePrime(mersenne, _pow):
  "Lucas–Lehmer primality test for Mersenne numbers"

  # This test applies only for odd powers, 
  # so we need to successfully pass it for the only one even prime - 2
  if _pow == 2: return True

  S = 4
  i = 1
  while (i != _pow - 1):
    S = (S*S - 2) % mersenne
    i += 1
    
  return S == 0

def MersennePrimesTillN (n):  
  _pow = 2
  mersenne = 3
  i = 0
  while (i < n):
    if (isMersennePrime(mersenne, _pow)): print(mersenne); i += 1
    _pow += 1
    mersenne = 2**_pow - 1


print('''----------------------------------------------------------
This programm generates a sequence of Mersenne primes up to N
----------------------------------------------------------''')
n = int(input('Enter N value: '))
assert n > 0

MersennePrimesTillN(n)
