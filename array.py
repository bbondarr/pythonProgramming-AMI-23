import random

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
    k = len(lst) - 1; i = 0

    while k > 1:
        while i+k <= len(lst):
            if (isAlternation(lst[i:i+k]) 
                and not i in reservedIndexes): 

                print('ALTERNATION SUBLIST -', lst[i:i+k])
                reservedIndexes += list(range(i, i+k))
                temp = lst[i:i+k]; temp.reverse()
                res[i:i+k] = temp                   
                i += k
            else: i += 1 
        k -= 1; i = 0
    
    return res    

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
        try: 
            # Input
            size = int(input('Enter list size: '))
            if (size <= 0): 
                print('Size must be greater than zero')
                continue
            maxValue = int(input('Enter maximal value of an element: '))
            minValue = int(input('Enter minimal value of an element: '))
            
            # List generation
            lst = [random.randint(minValue, maxValue) 
            for i in range(0, size)]

            # Programming task
            print('Your list:', lst, '\n')
            print('\nREVERSED LIST -', alternationsReverse(lst))
            break
        except ValueError:
            print('All input data must have an integer value\n')
            continue

def generateFromInput():
    while True:
        try: 
            # Input
            lst = [int(item) 
            for item in input("Enter the list items: ").split()] 

            # Programming task
            print('Your list:', lst, '\n')
            lst = alternationsReverse(lst)
            print('\nREVERSED LIST -', lst)
            break
        except ValueError:
            print('All input data must have an integer value\n')
            continue

menu()