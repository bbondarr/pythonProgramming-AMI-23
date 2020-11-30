import re
from datetime import date    

from flask_login import current_user


class Validation:
    def __init__(self): 
        pass

    @staticmethod
    def validateID(val):
        try:
            val = int(val)
            if val <= 0:
                 raise ValueError('ID must be a postitve integer')  
        except ValueError: 
            raise ValueError('ID must be a postitve integer')            

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
                if val > date.today():
                    raise ValueError('Bad Date value')
            except ValueError:
                raise ValueError('Bad Date value')
            func(_self, val)

        return inner

    @staticmethod
    def validateTwoDates(func):
        def inner(val1, val2):
            if val1 > val2:
                raise ValueError('Bad Date values')
            func(val1, val2)

        return inner

    @staticmethod
    def validateNotNoneProduct(product):
        if product is None:
            raise AttributeError('No product with such ID')

    @staticmethod
    def validateUser(User, val):
        if User.query.filter(User.email == val).first():
            raise AttributeError('User with such email already exists. Try logging in.')

    @staticmethod
    def validateLogin(func):
        def inner(*args):
            if not current_user.is_authenticated:
                raise ValueError('Only logged in users can view the data')
            func(*args)

        return inner