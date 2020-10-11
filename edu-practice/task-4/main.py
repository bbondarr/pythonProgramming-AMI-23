from Iterator import MersennePrimesIterator
from generator import MersennePrimesGenerator

def menu(): 
    print('-' * 58)
    print('This programm generates a sequence of Mersenne primes up to N')
    print('-' * 58)

    while True:
        try:
            n = input('Enter N value or type \'quit()\': ')
            if n == 'quit()': break
            n = validateN(n)
        except ValueError as ve: 
            print(ve.args[0]); continue
        print('-' * 58)

        while True:
            print('In which way do you want to generate the sequence?\n',
            '\'1\'- Iteraton\n',
            '\'2\'- Generator\n',
            '\'back()\' - Choose N again:')
            menuChoise = input()
    
            if menuChoise == '1': 
                print('-'*58)
                _iter = MersennePrimesIterator(n)
                for i in _iter:
                    print(i)
                print('-'*58)

            elif menuChoise == '2': 
                print('-'*58)
                for i in MersennePrimesGenerator(n):
                    print(i)
                print('-'*58)

            elif menuChoise == 'up()': break
            else: print('Enter 1, 2 or quit()')

def validateN(val):
    try:
        val = int(val)
        if val <= 0: 
            raise ValueError('N must be a positive integer') 
    except ValueError:
        raise ValueError('N must be a positive integer')

    return val

menu()