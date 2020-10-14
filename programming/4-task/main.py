from ProductContainer import ProductContainer
from Product import Product

def mainMenu():
    c = ProductContainer()

    print('-' * 50)
    print('Welcome to Product / Product Collection menu!')
    while True:
        print('-' * 50)
        print('''Choose one of the following opeartions:
    1 - Read collection from file
    2 - Print all products
    3 - Add a product from input
    4 - Delete product by ID
    5 - Find product
    6 - Sort the container
    7 - Edit product
    8 - Write into file
    9 - Exit''')
        print('-' * 50)

        menuChoise = input()
        try:
            if (menuChoise == '1'): readFromFileMenu(c)
            elif (menuChoise == '2'): print(c)
            elif (menuChoise == '3'): addMenu(c)
            elif (menuChoise == '4'): delMenu(c)
            elif (menuChoise == '5'): findMenu(c)
            elif (menuChoise == '6'): sortMenu(c)
            elif (menuChoise == '7'): editMenu(c)
            elif (menuChoise == '8'): writeMenu(c)
            elif (menuChoise == '9'): break
            else: print('-' * 50, 'Bad value')
        except (NameError, ValueError, AttributeError) as err:
            print(str(err))

def readFromFileMenu(c):
    fn = input('Enter filename (json/txt): ')
    c.readFromFile(fn)
    print('Collection succesfully read!')

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
    attr = input('Enter attribute to sort by: ')
    c.sort(attr)
    print('Collection succesfully sorted!')

def editMenu(c):
    _id = input('Enter ID: ') 
    attr = input('Enter attribute you want to change: ')
    val = input('Enter new value: ')
    c.edit(_id, attr, val)
    print('Product succesfully edited!')

def writeMenu(c):
    fn = input('Enter filename: ')
    c.writeIntoFile(fn)
    print('Collection succesfully written!')


mainMenu()
