from Context import Context, v
from strategies.IteratorStrategy import IteratorStrategy
from strategies.ReadFileStrategy import ReadFileStrategy
from algorithm import alternationsReverse

def menu():
    c = Context()

    print('-'*60)
    print('Welcome to pattern \'Strategy\' menu!')
    while True:
        print('-'*60)
        print('Choose one of the following options:\n',
        '1 - Choose \'Read From File\' strategy\n',
        '2 - Choose \'Generate using Iterator\' strategy\n',
        '3 - Generate list\n',
        '4 - Delete element by index\n',
        '5 - Delete element using slice\n', 
        '6 - Reverse alternations\n',
        '7 - Print the list\n',
        '8 - Exit menu')
        menuChoise = input()
        try:
            if (menuChoise == '1'): 
                c.setStrategy(ReadFileStrategy())
                print('Strategy set to \''+c.strategy()+'\'!')
            elif (menuChoise == '2'): 
                c.setStrategy(IteratorStrategy())
                print('Strategy set to \''+c.strategy()+'\'!')
            elif (menuChoise == '3'): generateMenu(c)
            elif (menuChoise == '4'): deleteMenu(c)
            elif (menuChoise == '5'): sliceMenu(c)
            elif (menuChoise == '6'): methodMenu(c)
            elif (menuChoise == '7'): print(c.lst())
            elif (menuChoise == '8'): break
            else: print('-' * 60+'\n', 'Bad value')
        except (AttributeError, ValueError, IndexError, FileNotFoundError) as err:
            print(str(err))

@v.validateContext
def generateMenu(c):
    if c.strategy() == 'readfile':
        pos = input('Enter the start position (0 required for the 1st time): ')
        if len(c.lst()) == 0: pos = 0; print('Set to 0')
        else: pos = v.validatePositiveInt(pos, 'Start position')

        fn = input('Enter filename (.txt): ')
        fn = v.validateFileName(fn)

        c.executeStrategy(pos, fn)

    elif c.strategy() == 'iterator':
        pos = input('Enter the start position (0 required for the 1st time): ')
        if len(c.lst()) == 0: pos = 0; print('Set to 0')
        else: pos = v.validatePositiveInt(pos, 'Start position')

        n = input('Enter quantity of numbers you want to add: ')
        n = v.validatePositiveInt(n, 'Quantity')

        c.executeStrategy(pos, n)

    print('Collection succesfully generated!')

@v.validateContext
@v.validateContextList
def deleteMenu(c):
    pos = int(input('Enter position of the element you want to delete: '))
    c.lst().pop(pos)
    print('Item succesfully deleted!')

@v.validateContext
@v.validateContextList
def sliceMenu(c):
    start = input('Enter start position of deletion: ')
    end = input('Enter end position of deletion: ')
    start = v.validatePositiveInt(start, 'Start')
    end = v.validatePositiveInt(end, 'End')
    if start > end or end >= len(c.lst()):
        raise ValueError('Bad index value')

    for i in range(end-start+1):
        c.lst().pop(start)

    print('Items succesfully deleted!')

@v.validateContext
@v.validateContextList
def methodMenu(c):
    print(alternationsReverse(c.lst()))

menu()