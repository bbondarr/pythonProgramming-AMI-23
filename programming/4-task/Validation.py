import re
from datetime import date

class Validation:
    def __init__(self): 
        pass

    def validateFloat(self, val, _str):
        try:
            val = float(val)
        except ValueError: 
            raise ValueError(_str+' must have a float value')
        
        return val        

    def validateFloatInRange(self, val, _str):
        val = self.validateFloat(val, _str)
        MIN_VAL, MAX_VAL = 0, 5000
        if not (MIN_VAL < val and val <= MAX_VAL): 
            raise ValueError(_str+' must be less than %d' %(MAX_VAL))

        return val

    def validateStr(self, val, _str):
        if not isinstance(val, str):
            raise ValueError(_str+' must have a string value')
        # if re.search(r'[^A-Za-z ]+', val) is not None: 
        #     raise ValueError(_str+' must contain only letters')
        
        return val     

    def validateURL(self, val, _str):
        val = self.validateStr(val, _str)
        regexSrch = re.search(r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)', val)
        if regexSrch is None: 
            raise ValueError('Bad URL for '+_str)
        
        return val 

    def validateDate(self, val, _str):
        if isinstance(val, str):
            [yyyy, mm, dd] = val.split('-')
            val = date(int(yyyy), int(mm), int(dd))
        if not isinstance(val, date):
            raise ValueError(_str+' must have a date value')

        return val

    def validateFileName(self, val, _str='filename'):
        if not isinstance(val, str):
            raise ValueError(_str+' must have a string value')        
        if  not (val.endswith('.json') or val.endswith('.txt')):
            raise ValueError(_str+' must be json or txt format')

        return val

    def validateProduct(self, val, _str='Product'):
        self.validateStr(val.getTitle(), 'Title')
        self.validateFloatInRange(val.getPrice(), 'Price')
        self.validateStr(val.getDescription(), 'Description')
        self.validateURL(val.getImageURL(), 'Image URL')
        self.validateDate(val.getCreatedAt(), 'Created At')
        self.validateDate(val.getUpdatedAt(), 'Updated At')
        
        return val