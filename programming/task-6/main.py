from ProductContainer import ProductContainer
from Product import Product

def mainMenu():
    c = ProductContainer()
    c.readFromFile('products.json')

    print('-' * 50)
    print('Welcome to Product / Product Collection menu!')
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
    8 - Exit''')
        print('-' * 50)

        menuChoise = input()
        if (menuChoise == '1'): print(c)
        elif (menuChoise == '2'): addMenu(c)
        elif (menuChoise == '3'): delMenu(c)
        elif (menuChoise == '4'): findMenu(c)
        elif (menuChoise == '5'): sortMenu(c)
        elif (menuChoise == '6'): editMenu(c)
        elif (menuChoise == '7'): writeMenu(c)
        elif (menuChoise == '8'): break
        else: print('-' * 50, 'Bad value')


def addMenu(_c):
    t = input('Enter Product title (str): ')
    i = input('Enter Product image URL (url str): ')
    p = input('Enter Product price (float): ')
    c = input('Enter Product creation date (date str): ')
    u = input('Enter Product update date (date str): ')
    d = input('Enter Product description (str): ')
    
    _c.add(Product(t, i, p, c, u, d))
    print('Product succesfully added!')

def delMenu(c):
    _id = input('Enter ID: ')    
    c.delete(_id)
    print('Product succesfully deleted!')

def findMenu(c):
    query = input('Enter search query: ')
    found = c.find(query)
    print('Search results:\n', found)

def sortMenu(c):
    attr = input('Enter attribute to sort by:')
    c.sort(attr)
    print('Collection succesfully sorted!')

def editMenu(c):
    _id = input('Enter ID: ') 
    attr = input('Enter attribute you want to change: ')
    val = input('Enter new value: ')
    c.edit(_id, attr, val)
    print('Product succesfully edited!')

def writeMenu(c):
    fn = input('Enter file name:')
    c.writeIntoFile(fn)
    print('Collection succesfully written!')

mainMenu()
