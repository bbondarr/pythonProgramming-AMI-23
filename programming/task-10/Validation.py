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
    def validateInt(func):
        def inner (_self, val):
            try:
                val = round(int(val), 2)
                func(_self, val)
            except ValueError: 
                raise ValueError('Value must be integer type')            

        return inner         

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
    def validateMail(func):
        def inner (_self, val):
            regexSrch = re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", val)
            if regexSrch is None: 
                raise ValueError('Bad Email value')            
            func(_self, val)

        return inner


    def validatePassword(func):
        def inner (_self, val):
            regexSrch = re.search(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", val)
            if regexSrch is None: 
                raise ValueError('Bad password (At least 8 characters, 1 letter and 1 number')            
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
    def validateNotNoneObject(product):
        if product is None:
            raise AttributeError('No object with such ID')

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