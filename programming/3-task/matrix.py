def runAndValidate():
    print('-' * 58, 
    '\nThis programm generates an incrementing square matrix of size N\n', 
    '-' * 58)
    while True: 
        # Input
        n = input('Enter N value or type \'quit()\' to exit programm: ')
        print('-' * 63)
        if (n == 'quit()'): return

        # Validate
        n = validateN(n, 'Size')
        if n is False: continue

        print('-' * 63)
        m = createMatrix(n)
        for i in range(n): print(m[i])

def validateN(val, str):
    try:
        val = int(val)
        if not val > 0: 
            print(str+' must be greater than zero\n', '-' * 63)
            val = False
    except ValueError: 
        print(str+' must have an integer value\n', '-' * 63)
        val = False
    
    return val 

def createMatrix(n):
    matrix = []
    elem = 1
    # c - multiplicative constant
    for c in range(1, n+1):
        row = list(range(elem, c*n + 1))
        elem += n
        matrix.append(row)

    return matrix

runAndValidate()