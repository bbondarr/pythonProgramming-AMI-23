import random
from LinkedList import *

# Algorithm implementation
def isAlternation(lst):
    """Checks whether the list is a sequence of alternations f.e. [-3, 2, -1, 10] - True"""
    for i in range(1, len(lst)):
        if not ((lst[i-1] >= 0 and lst[i] < 0) 
            or (lst[i-1] < 0 and lst[i] >= 0)):
            return False
    return True

def alternationsReverse(lst):
    res = lst.copy()
    reservedIndexes = []
    k = len(lst); i = 0

    while k > 1:
        while i+k <= len(lst):
            if (isAlternation(lst[i:i+k]) 
                and not i in reservedIndexes): 

                print('ALTERNATION SUBLIST - ', end='')
                lst[i:i+k].print()

                reservedIndexes += list(range(i, i+k))
                temp = lst[i:i+k]; temp.reverse()
                res[i:i+k] = temp                   
                i += k
            else: i += 1 
        k -= 1; i = 0
    
    return res    


# Menu implementation
def menu():
    while True:
        print('-' * 50)
        print('This programm finds the sequences of alterations in the list and reverses them')
        print('''Choose your way of list input:
    1 - Enter list size and randomly generate a list
    2 - Enter your list
    3 - Exit programm''')
        print('-' * 50)

        menuChoise = input()
        if (menuChoise == '1'): generateRandom()
        elif (menuChoise == '2'): generateFromInput()
        elif (menuChoise == '3'): break
        else: print('-' * 50, '\nEnter \'1\' or \'2\' or \'3\'')

def generateRandom():
    while True: 
        # Input
        size = input('Enter list size: ')
        maxValue = input('Enter maximal value of an element: ')
        minValue = input('Enter minimal value of an element: ')

        # Validation
        size = validateN(size, 'Size')
        maxValue = validateZ(maxValue, 'Max value')
        minValue = validateZ(minValue, 'Min value')
        if (size is False or maxValue is False or minValue is False):
            continue
            
        # List generation
        lst = [random.randint(minValue, maxValue) 
        for i in range(0, size)]
        lst = LinkedList(lst)

        # Programming task
        print('Your list: ', end='')
        lst.print()
        lst = alternationsReverse(lst)
        print('\nREVERSED LIST - ', end='')
        lst.print()
        break

def generateFromInput():
    while True:
        # Input
        lst = [item for item in input("Enter the list items: ").split()]

        # Validation
        flag = True
        for i in range(len(lst)): 
            lst[i] = validateZ(lst[i], 'List elements')
            if lst[i] is False: flag = False; break

        if not flag: continue

        lst = LinkedList(lst)

        # Programming task
        print('Your list: ', end='')
        lst.print()
        lst = alternationsReverse(lst)
        print('\nREVERSED LIST - ', end='')
        lst.print()
        break


# Validation
def validateZ(val, str):
    try:
        val = int(val)
    except ValueError: 
        print(str+' must have an integer value')
        val = False
    return val 

def validateN(val, str):
    val = validateZ(val, str)
    if not val > 0: 
        print(str+' must be greater than zero')
        val = False
    return val


menu()