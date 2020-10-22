from Validation import Validation as v

class Time:
    def __init__(self, hour, minute):
        self.__hour = v.validateHour(hour)
        self.__minute = v.validateMinute(minute)

    def __str__(self):
        return str(self.__hour) + ':' + str(self.__minute)

    def getHour(self):
        return self.__hour

    