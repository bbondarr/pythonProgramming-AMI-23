import re
from datetime import date    

class Validation:
    def __init__(self): 
        pass

    @staticmethod
    def validateFloat(func):
        def inner (_self, val):
            try:
                val = round(float(val), 2)
                func(_self, val)
            except ValueError: 
                raise ValueError('Value must be float type')            

        return inner

    @staticmethod
    def validateFloatInRange(func):
        def inner (_self, val):
            MIN_VAL, MAX_VAL = 0, 5000
            if not (MIN_VAL < val and val <= MAX_VAL): 
                raise ValueError('Value must be less than %d' %(MAX_VAL))   
            func(_self, val)        

        return inner      

    @staticmethod
    def validateStr(func):
        def inner (_self, val):
            if not isinstance(val, str):
                raise ValueError('Value must be str type')
            func(_self, val)            

        return inner     

    @staticmethod
    def validateTitle(func):
        def inner (_self, val):
            if re.search(r'[^A-Za-z ]+', val) is not None: 
                raise ValueError('Value must contain only letters')    
            func(_self, val)            

        return inner

    @staticmethod
    def validateURL(func):
        def inner (_self, val):
            regexSrch = re.search(r'^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+$', val)
            if regexSrch is None: 
                raise ValueError('Bad URL value')            
            func(_self, val)

        return inner

    @staticmethod
    def validateDate(func):
        def inner (_self, val):
            try:
                if isinstance(val, str):
                    [yyyy, mm, dd] = val.split('-')
                    val = date(int(yyyy), int(mm), int(dd))
            except ValueError:
                raise ValueError('Value must be Date type')
            func(_self, val)

        return inner

    @staticmethod
    def validateTwoDates(func):
        def inner(_self, val1, val2):
            if val1 > val2:
                raise ValueError('Bad Date values')
            func(_self, val1, val2)

        return inner

    @staticmethod
    def validateFileName(func):
        def inner (_self, val): 
            if  not (val.endswith('.json') or val.endswith('.txt')):
                raise ValueError('Value must be json or txt format')
            func(_self, val)

        return inner

    @staticmethod
    def validateProduct(func):
        def inner (_self, val):
            Validation.validateStr(func)
            Validation.validateFloatInRange(func)
            Validation.validateStr(func)
            Validation.validateURL(func)
            Validation.validateDate(func)
            Validation.validateDate(func)
            func(_self, val)
            return val

        return inner