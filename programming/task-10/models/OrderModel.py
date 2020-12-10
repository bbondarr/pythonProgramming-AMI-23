from datetime import date

from flask_login import UserMixin

from app import db
from Validation import Validation as v


class Order(UserMixin, db.Model):
    __tablename__ = 'Orders'
    id = db.Column('id', db.Integer, primary_key=True)
    userID = db.Column('userID', db.Integer, db.ForeignKey("Users.id"), nullable=False)
    productID = db.Column('productID', db.Integer, db.ForeignKey("Products.id"), nullable=False)
    amount = db.Column('amount', db.Integer, nullable=False)
    date = db.Column('date', db.String, nullable=False)


    def __init__(self, productID, amount, userID=None):
        if userID:
            self.setUserID(userID)
        self.setProductID(productID)
        self.setAmount(amount)
        self.setDate()

    @v.validateID
    def setUserID(self, val):
        self.userID = val

    @v.validateID
    def setProductID(self, val):
        self.productID = val

    @v.validateQuantity
    def setAmount(self, val):
        self.amount = val

    def setDate(self):
        self.date = date.today()

    @staticmethod
    def attributes():
        return [a for a in dir(Order) 
                if (not a.startswith('get') 
                and not a.startswith('set') 
                and not a.startswith('_') 
                and not a.startswith('is')
                and a != 'query' and a != 'metadata'  
                and a != 'product' and a != 'user'
                and not callable(getattr(Order, a)))]