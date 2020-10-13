import re
from datetime import date

class Validation:
    def __init__(self): 
        pass

    @staticmethod
    def validateFloat(val, _str):
        try:
            val = round(float(val), 2)
        except ValueError: 
            raise ValueError(_str+' must have a float value')
        
        return val        

    @staticmethod
    def validateFloatInRange(val, _str):
        val = Validation.validateFloat(val, _str)
        MIN_VAL, MAX_VAL = 0, 5000
        if not (MIN_VAL < val and val <= MAX_VAL): 
            raise ValueError(_str+' must be less than %d' %(MAX_VAL))

        return val

    @staticmethod
    def validateStr(val, _str):
        if not isinstance(val, str):
            raise ValueError(_str+' must have a string value')
        # if re.search(r'[^A-Za-z ]+', val) is not None: 
        #     raise ValueError(_str+' must contain only letters')
        
        return val     

    @staticmethod
    def validateURL(val, _str):
        val = Validation.validateStr(val, _str)
        regexSrch = re.search(r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)', val)
        if regexSrch is None: 
            raise ValueError('Bad URL for '+_str)
        
        return val 

    @staticmethod
    def validateDate(val, _str):
        if isinstance(val, str):
            [yyyy, mm, dd] = val.split('-')
            val = date(int(yyyy), int(mm), int(dd))
        if not isinstance(val, date):
            raise ValueError(_str+' must have a date value')

        return val

    @staticmethod
    def validateFileName(val, _str='filename'):
        if not isinstance(val, str):
            raise ValueError(_str+' must have a string value')        
        if  not (val.endswith('.json') or val.endswith('.txt')):
            raise ValueError(_str+' must be json or txt format')

        return val

    @staticmethod
    def validateProduct(val, _str='Product'):
        Validation.validateStr(val.getTitle(), 'Title')
        Validation.validateFloatInRange(val.getPrice(), 'Price')
        Validation.validateStr(val.getDescription(), 'Description')
        Validation.validateURL(val.getImageURL(), 'Image URL')
        Validation.validateDate(val.getCreatedAt(), 'Created At')
        Validation.validateDate(val.getUpdatedAt(), 'Updated At')
        
        return val