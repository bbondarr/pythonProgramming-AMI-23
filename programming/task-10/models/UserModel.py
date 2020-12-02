import enum

from flask_login import UserMixin

from app import db
from Validation import Validation as v


class RoleEnum(enum.Enum):
    admin = 1
    user = 2


class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    id = db.Column('id', db.Integer, primary_key=True)
    firstName = db.Column('firstName', db.String, nullable=False)
    lastName = db.Column('lastName', db.String, nullable=False)
    email = db.Column('email', db.String, nullable=False, unique=True)
    password = db.Column('password', db.String, nullable=False)
    role = db.Column('role', db.Enum('admin', 'user'), default='admin', nullable=False)

    products = db.relationship('Product', backref='user')
    orders = db.relationship('Order', backref='user')


    def __init__(self, firstName, lastName, email, password, role='admin'):
        self.setFirstName(firstName)
        self.setLastName(lastName)
        self.setEmail(email)
        self.setPassword(password)
        self.setRole(role)

@staticmethod
def attributes():
    return [a for a in dir(User) 
            if (not a.startswith('get') 
            and not a.startswith('set') 
            and not a.startswith('_') 
            and not a.startswith('is')
            and a != 'query' and a != 'metadata' 
            and not callable(getattr(User, a)))]

    @v.validateTitle
    def setFirstName(self, val):
        self.firstName = val

    @v.validateTitle
    def setLastName(self, val):
        self.lastName = val

    @v.validateStr
    @v.validateMail
    def setEmail(self, val):
        self.email = val

    @v.validateStr
    @v.validatePassword
    def setPassword(self, val):
        self.password = val

    def setRole(self, val):
        self.role = val

