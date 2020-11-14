from Validation import Validation as v
import json
from collections import namedtuple

class BlablacarBooking:
    def __init__(self, name, noP, startTime, endTime, startPlace, endPlace):
        self.setName(name)
        self.setNumOfP(noP)
        self.setStartTime(startTime)
        self.setEndTime(endTime)
        self.setStartPlace(startPlace)
        self.setEndPlace(endPlace)

    def __str__(self):
        return ('Driver Name: '+str(self.__name)+
            '\nNum of Passengers: '+str(self.__noP)+
            '\nStart Time: '+str(self.__startTime)+
            '\nEnd Time: '+str(self.__endTime)+
            '\nStart Place: '+str(self.__startPlace)+
            '\nEnd Place: '+str(self.__endPlace))  

    @staticmethod
    def getAttributes():
        return [a[3].lower()+a[4:] for a in BlablacarBooking.getGetters()]
    @staticmethod
    def getGetters():
        return [a for a in dir(BlablacarBooking) 
                if (a.startswith('get') 
                and a != 'getAttributes' and a != 'getGetters' 
                and callable(getattr(BlablacarBooking, a)))]

    def getName(self):
        return self.__name
    def getNoP(self):
        return self.__noP
    def getStartTime(self):
        return self.__startTime
    def getEndTime(self):
        return self.__endTime
    def getStartPlace(self):
        return self.__startPlace
    def getendPlace(self):
        return self.__endPlace

    @v.validateName
    def setName(self, val):
        self.__name = val

    @v.validateInt
    @v.validateNumOfP
    def setNumOfP(self, val):
        self.__noP = val


    def setStartTime(self, val):
        val = namedtuple("Time", val.keys())(*val.values())
        v.validateHour(val.hour)
        v.validateMinute(val.minute)
        self.__startTime = val


    def setEndTime(self, val):
        val = namedtuple("Time", val.keys())(*val.values())
        v.validateHour(val.hour)
        v.validateMinute(val.minute)
        self.__endTime = val

    @v.validateName
    def setStartPlace(self, val):
        self.__startPlace = val

    @v.validateName
    def setEndPlace(self, val):
        self.__endPlace = val

class DictToObject(object):

    def __init__(self, dictionary):
        def _traverse(key, element):
            if isinstance(element, dict):
                return key, DictToObject(element)
            else:
                return key, element

        objd = dict(_traverse(k, v) for k, v in dictionary.iteritems())
        self.__dict__.update(objd)