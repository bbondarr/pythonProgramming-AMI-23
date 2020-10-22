import re
from datetime import date    

class Validation:
    def __init__(self): 
        pass

    @staticmethod
    def validateInt(func):
        def inner (_self, val):
            try:
                val = int(val)
                func(_self, val)
            except ValueError: 
                raise ValueError('Value must be integer type')            

        return inner

    @staticmethod
    def validateNumOfP(func):
        def inner (_self, val):
            MIN_VAL, MAX_VAL = 1, 4
            if not (MIN_VAL <= val and val <= MAX_VAL): 
                raise ValueError('Value must be less than %d' %(MAX_VAL))   
            func(_self, val)                   

        return inner

    @staticmethod
    def validateHour(func):
        def inner (val):
            MIN_VAL, MAX_VAL = 0, 23
            if not (MIN_VAL <= val and val <= MAX_VAL): 
                raise ValueError('Value must be less than %d' %(MAX_VAL))   
            func(val)        

        return inner      

    @staticmethod
    def validateMinute(func):
        def inner (val):
            MIN_VAL, MAX_VAL = 0, 59
            if not (MIN_VAL <= val and val <= MAX_VAL): 
                raise ValueError('Value must be less than %d' %(MAX_VAL))   
            func(val)        

        return inner 

    @staticmethod
    def validateStr(func):
        def inner (_self, val):
            if not isinstance(val, str):
                raise ValueError('Value must be str type')
            func(_self, val)            

        return inner     

    @staticmethod
    def validateName(func):
        def inner (_self, val):
            if not isinstance(val, str):
                raise ValueError('Value must be str type')
            if re.search(r'[^A-Za-z ]+', val) is not None: 
                raise ValueError('Value must contain only letters')    
            func(_self, val)            

        return inner
    
    # @staticmethod
    # def validateENUM(func):
    #     def inner(_self, val):
    #         if str(val).lower() not in enums.ENUM.__members__:
    #             print("Value is not listed in Enum")
    #         func(_self, val)

    #     return inner

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
        
            func(_self, val)
            return val

        return inner
