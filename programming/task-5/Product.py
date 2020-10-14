import json
from datetime import date
from Validation import Validation as v

class Product:
    def __init__(self, 
        title, imageURL, price, createdAt, updatedAt, description, ID=None):

        self.__ID = str(id(self)) if ID is None else str(ID)
        self.setTitle(title)
        self.setImageURL(imageURL)
        self.setPrice(price)
        self.setDescription(description)
        self.setCreatedAt(createdAt)
        self.setUpdatedAt(updatedAt)

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

    @v.validateTitle
    def setTitle(self, val): 
        self.__title = val
        self.__updatedAt = date.today()
    
    @v.validateURL
    def setImageURL(self, val):
        self.__imageURL = val
        self.__updatedAt = date.today()
    
    @v.validateFloat
    @v.validateFloatInRange
    def setPrice(self, val): 
        self.__price = val
        self.__updatedAt = date.today()
    
    @v.validateStr
    def setDescription(self, val): 
        self.__description = val
        self.__updatedAt = date.today()

    @v.validateDate
    def setCreatedAt(self, val):
        self.__createdAt = val
        self.__updatedAt = date.today()
    
    @v.validateDate
    def setUpdatedAt(self, val):
        self.__updatedAt = val