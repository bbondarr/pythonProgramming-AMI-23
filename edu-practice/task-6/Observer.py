from Validation import Validation as v

class Observer:
    def __init__(self, fn, events):
        self.fn = v.validateFileName(fn)
        self.events = events

    def add(self, event):
        Logger.printToFile(self.fn, event)

    def remove(self, event):
        Logger.printToFile(self.fn, event)

    def change(self, event):
        Logger.printToFile(self.fn, event)

class Event:
    def __init__(self):
        pass


class Logger:
    @staticmethod
    def printToFile(fn, method, primary, elems, new):
        with open(fn) as file:
            if method == 'add':
                file.write('added') 
            elif method == 'remove':
                file.write('removed') 