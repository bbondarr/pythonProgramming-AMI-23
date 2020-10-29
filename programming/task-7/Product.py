import json
from datetime import date
from Validation import Validation as v

class Product:
    def __init__(self, 
        title, imageURL, price, createdAt, updatedAt, description, iD=None):

        self.__iD = str(id(self)) if iD is None else str(iD)
        self.setTitle(title)
        self.setImageURL(imageURL)
        self.setPrice(price)
        self.setDescription(description)
        self.setCreatedAt(createdAt)
        self.setUpdatedAt(updatedAt)

        self.compareDates(self.__createdAt, self.__updatedAt)

    def __str__(self):
        return ('ID: '+str(self.__iD)+
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
            copy[a] = str(getattr(self, '_Product__'+a)) 
            
        return json.dumps(copy, indent=4)      

    def copy(self):
        return Product(self.__title, 
                        self.__imageURL, 
                        self.__price, 
                        self.__createdAt, 
                        self.__updatedAt, 
                        self.__description)

    def getID(self):
        return self.__iD
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

    @staticmethod
    def getAttributes():
        return [a[3].lower()+a[4:] for a in Product.getGetters()]
    @staticmethod
    def getGetters():
        return [a for a in dir(Product) 
                if (a.startswith('get') 
                and a != 'getAttributes' and a != 'getGetters' 
                and callable(getattr(Product, a)))]

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
        self.compareDates(self.__createdAt, val)
        self.__updatedAt = val

    @v.validateTwoDates
    def compareDates(self, date1, date2):
        pass