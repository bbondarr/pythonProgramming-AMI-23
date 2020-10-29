from collections import deque

class Caretaker:
    def __init__(self, originator):
        self.__undoQ = deque(maxlen=5)
        self.__redoQ = deque(maxlen=5)
        self.__originator = originator

    def backup(self, mode='undo'):
        if mode == 'undo':
            if len(self.__undoQ) == self.__undoQ.maxlen:
                self.__undoQ.popleft()
            self.__undoQ.append(self.__originator.save())

        elif mode == 'redo':
            if len(self.__redoQ) == self.__redoQ.maxlen:
                self.__redoQ.popleft()
            self.__redoQ.append(self.__originator.save())

    def undo(self):
        if not len(self.__undoQ):
            raise AttributeError('No actions to undo (the limit is 5)')
        if len(self.__redoQ) == self.__redoQ.maxlen:
            self.__redoQ.popleft()

        self.backup('redo')
        memento = self.__undoQ.pop()
        self.__originator.restore(memento)

    def redo(self):
        if not len(self.__redoQ):
            raise AttributeError('No actions to redo (the limit is 5)')
        if len(self.__undoQ) == self.__undoQ.maxlen:
            self.__undoQ.popleft()

        self.backup()
        memento = self.__redoQ.pop()
        self.__originator.restore(memento)