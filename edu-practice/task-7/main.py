import threading

from Context import Context, v
from strategies.IteratorStrategy import IteratorStrategy
from strategies.ReadFileStrategy import ReadFileStrategy
from algorithm import alternationsReverse

from Observer import Observer, Event
from Logger import FileLogger

def menu():
    c1 = Context()
    c2 = Context()
    Observer.attach('add', FileLogger.logAdd)
    Observer.attach('remove', FileLogger.logRemove)
    Observer.attach('method', FileLogger.logMethodExecution)

    print('-'*60)
    print('Welcome to pattern \'Strategy\' menu!')
    print('First fill two lists with both strategies:')
    while True:
        try:
            print('-'*60)
            generateWithReadFile(c1)
            print('-'*60)
            generateWithIterator(c2)
            break
        except (AttributeError, ValueError, IndexError, FileNotFoundError) as err:
            print(str(err))

    while True:
        print('-'*60)
        print('Choose one of the following options:\n',
        '1 - Delete element by index\n',
        '2 - Delete element using slice\n',
        '3 - Reverse alternations\n',
        '4 - Print the list\n',
        '5 - Exit menu')
        menuChoise = input()
        try:
            if   (menuChoise == '1'): deleteMenu(c1, c2)
            elif (menuChoise == '2'): sliceMenu(c1, c2)
            elif (menuChoise == '3'): methodMenu(c1, c2)
            elif (menuChoise == '4'): printMenu(c1, c2)
            elif (menuChoise == '5'): break
            else: print('-' * 60+'\n', 'Bad value')
        except (AttributeError, ValueError, IndexError, FileNotFoundError) as err:
            print(str(err))


def generateWithReadFile(c):
    print('Please fill the list using \'readfile\' strategy:')
    c.setStrategy(ReadFileStrategy())
    former = c.lst().copy()

    pos = 0
    fn = input('Enter filename (.txt): ')
    fn = v.validateFileName(fn)

    c.executeStrategy(pos, fn)
    Event.update('add', former, pos, c.lst())
    print('Collection succesfully generated!')

def generateWithIterator(c):
    print('Please fill the list using \'iterator\' strategy:')
    c.setStrategy(IteratorStrategy())
    former = c.lst().copy()

    pos = 0
    n = input('Enter quantity of numbers you want to add: ')
    n = v.validatePositiveInt(n, 'Quantity')

    c.executeStrategy(pos, n)       
    Event.update('add', former, pos, c.lst())
    print('Collection succesfully generated!')

def deleteMenu(c1, c2):
    def delete(c, pos):
        former = c.lst().copy()
        c.lst().pop(pos)
        Event.update('remove', former, pos, c.lst())

    pos = int(input('Enter position of the element you want to delete: '))
    
    t1 = threading.Thread(target=delete, args=(c1, pos))
    t2 = threading.Thread(target=delete, args=(c2, pos))

    print('Thread 1 started...'); t1.start()
    print('Thread 2 started...'); t2.start()
    print('Thread 1 finished!');  t1.join()
    print('Thread 2 finished!');  t2.join()

    print('Item succesfully deleted!')

def sliceMenu(c1, c2):
    def _slice(c, start, end):
        if start > end or end >= len(c.lst()):
            raise ValueError('Bad index value')

        former = c.lst().copy()
        for _ in range(end-start+1):
            c.lst().pop(start)

        Event.update('remove', former, [start, end], c.lst())

    start = input('Enter start position of deletion: ')
    end = input('Enter end position of deletion: ')
    start = v.validatePositiveInt(start, 'Start')
    end = v.validatePositiveInt(end, 'End')
    
    t1 = threading.Thread(target=_slice, args=(c1, start, end))
    t2 = threading.Thread(target=_slice, args=(c2, start, end))

    print('Thread 1 started...'); t1.start()
    print('Thread 2 started...'); t2.start()
    print('Thread 1 finished!');  t1.join()
    print('Thread 2 finished!');  t2.join()

    print('Items succesfully deleted!')

def methodMenu(c1, c2):
    def method(c):
        former = c.lst().copy()
        c.setList(alternationsReverse(c.lst()))
        Event.update('method', former, c.lst())
        print(c.lst())

    t1 = threading.Thread(target=method, args=[c1])
    t2 = threading.Thread(target=method, args=[c2])

    print('Thread 1 started...'); t1.start()
    print('Thread 2 started...'); t2.start()
    print('Thread 1 finished!');  t1.join()
    print('Thread 2 finished!');  t2.join()

def printMenu(c1, c2):
    t1 = threading.Thread(target=print, args=c1.lst())
    t2 = threading.Thread(target=print, args=c2.lst())

    print('Thread 1 started...'); t1.start()
    print('Thread 2 started...'); t2.start()
    print('Thread 1 finished!');  t1.join()
    print('Thread 2 finished!');  t2.join()

menu()