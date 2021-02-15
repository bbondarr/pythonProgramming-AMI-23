from BlablacarBooking import BlablacarBooking
from Validation import Validation as v
import json

class BlablaList:
    def __init__(self, lst = None):
        self.__lst = [] if lst == None else lst

    def __str__(self):
        Str = '[\n'
        for b in self.__lst:
            Str += str(b) + '\n'
        Str += ']'

        return Str

    @v.validateStr
    @v.validateFileName
    def readFromFile(self, fn):
        with open(fn) as file:
            jsonLst = json.load(file)

        i = 0
        for _dict in jsonLst:
            i+=1
            try:
                p = BlablacarBooking(**{a:_dict.get(a) for a in BlablacarBooking.getAttributes()})
            except ValueError as ve:
                print('Booking %d Error: ' % (i) + str(ve)); continue

            self.__lst.append(p)

    def getTopHour(self):
        _max = self.__lst.count(lambda b: b.getStartTime().hour)
        copy = self.__lst.copy()
        filter(lambda b: b.getStartTime().hour == _max, copy)
        return [b.getStartTime().hour for b in copy]

    def getTopDriver(self):
        drivers = [[b.getName(), 0] for b in self.__lst]
        for b in self.__lst:
            for d in drivers:
                if b.getName() == d[0]:
                    d[1] += 1
        _max = ['', -1]
        for d in drivers:
            if d[1] > _max[1]:
                _max = d
        for b in self.__lst:
            if b.getName() == _max[0]:
                return str(_max[0]) +', '+str(_max[1])