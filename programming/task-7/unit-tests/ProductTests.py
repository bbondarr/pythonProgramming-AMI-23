import unittest

class ProductTest(unittest.TestCase):
    def setUp(self, product):
        self.product = product

    def testInit(self):
        pass

    def testStr(self):
        productStr = ('ID: '+str(self.product.getID())+
            '\nProduct: '+self.product.getTitle()+
            '\nImage URL: '+self.product.getImageURL()+
            '\nPrice: '+str(self.product.getPrice())+
            '\nCreated At: '+str(self.product.getCreatedAt())+
            '\nUpdated At: '+str(self.product.getUpdatedAt())+
            '\nDescription: '+self.product.getDescription())
            
        self.assertEqual(str(self.product), productStr)

    def testToJSON(self):
        pass

    def testGetters(self):
        pass

    def testSetters(self):
        pass