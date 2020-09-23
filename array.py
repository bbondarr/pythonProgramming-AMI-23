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

            # Edu practice task
            k = input('\nFind all the entries of K value\nEnter K value or type \'q\' to quit: ')
            if (k == 'q'): break
            k = int(k)

            indexLst = [i for i in range(0, len(lst))]
            sort(lst, indexLst)

            sortedIndexes = find(lst, k)
            print('\n%d is on position' % (k), end=' ')
            for i in sortedIndexes:
                print(indexLst[i], end=' ')
            print('\n')
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

            # Edu practice task
            k = input('\nFind all the entries of K value\nEnter K value or type \'q\' to quit: ')
            if (k == 'q'): break
            k = int(k)

            indexLst = [i for i in range(0, len(lst))]
            sort(lst, indexLst)
            print('Sorted list:', lst)

            sortedIndexes = find(lst, k)
            print('\n%d is on position' % (k), end=' ')
            for i in sortedIndexes:
                print(indexLst[i], end=' ')
            print('\n')
            break
        except ValueError:
            print('All input data must have an integer value\n')
            continue

def sort(lst, indLst):
    """Sorting two lists in terms of the first one"""
    for i in range(0, len(lst)):
        for j in range(0, len(lst)-1-i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                indLst[j], indLst[j + 1] = indLst[j + 1], indLst[j]

def find(lst, k):
    first = findFirst(lst, k)
    last = findLast(lst, k)
    print('\nAll %ds were found for %d operations' % (k, first[0]+last[0]))

    return list(range(first[1], last[1]+1))
      
def findFirst(lst, k):
    """Binary search algorithm for first K entry in the list"""
    first = -1
    low, top = 0, len(lst) - 1
    print('\nLooking for a first entry of %d' % (k))
    counter = 1
    
    while low <= top: 
        mid = low + (top - low) // 2
        
        print('%d. Checking if element is between pos %d and %d...' % (counter, low, top))
        counter+=1
        print('\tChecking if element is on pos %d...' % (mid))

        if (lst[mid] == k):
            first = mid
            top = mid - 1
            print('Found %d on pos %d!' % (k, mid))
        elif lst[mid] < k: 
            low = mid + 1
        else: 
            top = mid - 1 

    return [counter, first]

def findLast(lst, k):
    """Binary search algorithm for last K entry in the list"""
    last = -1
    low, top = 0, len(lst) - 1
    print('\nLooking for a last entry of %d' % (k))
    counter = 1

    while low <= top: 
        mid = low + (top - low) // 2

        print('%d. Checking if element is between pos %d and %d...' % (counter, low, top))
        counter+=1
        print('\tChecking if element is on pos %d...' % (mid))

        if (lst[mid] == k):
            last = mid
            low = mid + 1
            print('Found %d on pos %d!' % (k, mid))
        elif lst[mid] < k: 
            low = mid + 1
        else: 
            top = mid - 1

    return [counter, last]

menu()