from datetime import date

from app import db
from Validation import Validation as v


class Product(db.Model):
    __tablename__ = 'Products'
    iD = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String, nullable=False)
    imageURL = db.Column('imageURL', db.String, nullable=False)
    price = db.Column('price', db.Float, nullable=False)
    createdAt = db.Column('createdAt', db.String, nullable=False)
    updatedAt = db.Column('updatedAt', db.String, nullable=False)
    description = db.Column('description', db.Text, nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey("Users.id"))


    def __init__(self, 
        title, imageURL, price, createdAt, updatedAt, description, iD=None):

        if iD:  
            self.iD = str(iD)
        self.setTitle(title)
        self.setImageURL(imageURL)
        self.setPrice(price)
        self.setDescription(description)
        self.setCreatedAt(createdAt)
        self.setUpdatedAt(updatedAt)

        Product.compareDates(self.createdAt, self.updatedAt)

    @staticmethod
    def attributes():
        return [a for a in dir(Product) 
                if (not a.startswith('get') 
                and not a.startswith('set') 
                and not a.startswith('_') 
                and a != 'query' and a != 'metadata'
                and not callable(getattr(Product, a)))]

    @v.validateTitle
    def setTitle(self, val): 
        self.title = val
        self.updatedAt = date.today()
    
    @v.validateURL
    def setImageURL(self, val):
        self.imageURL = val
        self.updatedAt = date.today()
    
    @v.validateFloat
    @v.validateFloatInRange
    def setPrice(self, val): 
        self.price = val
        self.updatedAt = date.today()
    
    @v.validateStr
    def setDescription(self, val): 
        self.description = val
        self.updatedAt = date.today()

    @v.validateDate
    def setCreatedAt(self, val):
        self.createdAt = val
        self.updatedAt = date.today()
    
    @v.validateDate
    def setUpdatedAt(self, val):
        Product.compareDates(self.createdAt, val)
        self.updatedAt = val

    @staticmethod
    @v.validateTwoDates
    def compareDates(date1, date2):
        pass
