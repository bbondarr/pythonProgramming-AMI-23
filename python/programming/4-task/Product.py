import json
from datetime import date
from Validation import Validation as v, ERR_VALUE

class Product:
    def __init__(self, 
        title, imageURL, price, createdAt, updatedAt, description, ID=None):

        self.__ID = str(id(self)) if ID is None else str(ID)
        self.__title = v.validateTitle(title, 'Title')
        self.__imageURL = v.validateURL(imageURL, 'Image URL')
        self.__price = v.validateFloatInRange(price, 'Price')
        self.__createdAt = v.validateDate(createdAt, 'Created At')
        self.__updatedAt = v.validateDate(updatedAt, 'Updated At')
        self.__description = v.validateStr(description, 'Description')

        for a in self.getAttributes():
            if getattr(self, a) == ERR_VALUE:
                raise ValueError('Couldn\'t read Product from file')

    def __str__(self):
        return ('ID: '+str(self.__ID)+
            '\nProduct: '+self.__title+
            '\nImage URL: '+self.__imageURL+
            '\nPrice: '+str(self.__price)+
            '\nCreated At: '+str(self.__createdAt)+
            '\nUpdated At: '+str(self.__updatedAt)+
            '\nDescription: '+self.__description)

    def toJSON(self):
        attr = self.getAttributes()
        copy = {}
        for a in attr:
            copy[a.replace('_Product__', '')] = str(getattr(self, a)) 
            
        return json.dumps(copy, indent=4)      

    def getID(self):
        return self.__ID
    def getTitle(self): 
        return self.__title
    def getImageURL(self): 
        return self.__imageURL
    def getPrice(self): 
        return self.__price
    def getCreatedAt(self): 
        return self.__createdAt
    def getUpdatedAt(self):
        return self.__updatedAt
    def getDescription(self): 
        return self.__description

    def getAttributes(self):
        return [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
    def getGetters(self):
        return [a for a in dir(self) if a.startswith('get') and callable(getattr(self, a))]

    def setTitle(self, val): 
        val = v.validateStr(val, 'Title')
        self.__title = val
        self.__updatedAt = date.today()
    def setImageURL(self, val):
        val = v.validateURL(val, 'Image URL')
        self.__imageURL = val
        self.__updatedAt = date.today()
    def setPrice(self, val): 
        val = v.validateFloatInRange(val, 'Price')
        self.__price = val
        self.__updatedAt = date.today()
    def setDescription(self, val): 
        val = v.validateStr(val, 'Description')
        self.__description = val
        self.__updatedAt = date.today()