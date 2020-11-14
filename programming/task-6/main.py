from ProductContainer import ProductContainer
from Product import Product
from SnapshotCaretaker import Caretaker

def mainMenu():
    print('-' * 50)
    print('Welcome to Product / Product Collection menu!')
    while True:
        print('-' * 50)
        try:
            c = readFromFileMenu()
            ct = Caretaker(c)
            break
        except ValueError as ve:
            print(str(ve))
            
    while True:
        print('-' * 50)
        print('''Choose one of the following opeartions:
    1 - Print all products
    2 - Add a product from input
    3 - Delete product by ID
    4 - Find product
    5 - Sort the container
    6 - Edit product
    7 - Write into file
    8 - Undo last action
    9 - Redo last action
    10 - Exit''')
        print('-' * 50)

        menuChoise = input()
        try:
            if (menuChoise == '1'): print(c)
            elif (menuChoise == '2'): addMenu(c, ct)
            elif (menuChoise == '3'): delMenu(c, ct)
            elif (menuChoise == '4'): findMenu(c)
            elif (menuChoise == '5'): sortMenu(c, ct)
            elif (menuChoise == '6'): editMenu(c, ct)
            elif (menuChoise == '7'): writeMenu(c)
            elif (menuChoise == '8'): undoMenu(ct)
            elif (menuChoise == '9'): redoMenu(ct)
            elif (menuChoise == '10'): break
            else: print('-' * 50, '\nBad value')
        except (ValueError, NameError, FileNotFoundError, AttributeError) as err:
            print(str(err))


def readFromFileMenu():
    fn = input('Enter filename (json/txt): ')
    c = ProductContainer(fn)
    c.readFromFile(fn)
    print('Collection succesfully read!')
    return c

def addMenu(_c, ct):
    ct.backup()
    
    t = input('Enter Product title (str): ')
    i = input('Enter Product image URL (url str): ')
    p = input('Enter Product price (float): ')
    c = input('Enter Product creation date (date str): ')
    u = input('Enter Product update date (date str): ')
    d = input('Enter Product description (str): ')
    
    _c.add(Product(t, i, p, c, u, d))
    print('Product succesfully added!')

def delMenu(c, ct):
    ct.backup()

    _id = input('Enter ID: ')    
    c.delete(_id)
    print('Product succesfully deleted!')

def findMenu(c):
    query = input('Enter search query: ')
    found = c.find(query)
    print('Search results:\n', found)

def sortMenu(c, ct):
    ct.backup()

    attr = input('Enter attribute to sort by: ')
    c.sort(attr)
    print('Collection succesfully sorted!')

def editMenu(c, ct):
    ct.backup()

    _id = input('Enter ID: ') 
    attr = input('Enter attribute you want to change: ')
    val = input('Enter new value: ')
    c.edit(_id, attr, val)
    print('Product succesfully edited!')

def undoMenu(ct):
    ct.undo()
    print('Last action undone!')

def redoMenu(ct):   
    ct.redo()
    print('Last action redone!')

def writeMenu(c):
    fn = input('Enter filename: ')
    c.writeIntoFile(fn)
    print('Collection succesfully written!')


mainMenu()