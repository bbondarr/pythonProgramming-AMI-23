import unittest

from ProductContainer import Product, ProductContainer
from SnapshotCaretaker import Caretaker

class MenuTest(unittest.TestCase):
    def setUp(self):
        self.testList = testData
        self.container = ProductContainer()

        # For not writing 'self.container._ProductContainer__productList' all the time
        # and for primary filling
        self.lst = self.container._ProductContainer__productList
        for p in self.testList:
            self.lst.append(p)

        self.caretaker = Caretaker(self.container)

    def testAdd(self):
        # Adding elements in a loop
        for i, p in enumerate(self.testList, start=len(self.lst)):
            self.container.add(p)
            self.assertEqual(len(self.container), i+1)
            self.assertIn(p, self.lst)

        lameVals = [('123', 'test.com.ua', 49.50, '2020-01-01', '2020-04-04', 'test'),
                    ('ttl', 'ur^l.com.ua', 49.50, '2020-01-01', '2020-04-04', 'test'),
                    ('ttl', 'test.com.ua', 'str', '2020-01-01', '2020-04-04', 'test'),
                    ('ttl', 'test.com.ua', 49.50, '3030-01-01', '2020-04-04', 'test'),
                    ('ttl', 'test.com.ua', 49.50, '2020-01-01', '2002-04-04', 'test'),
                    ('ttl', 'test.com.ua', 49.50, '2020-01-01', '2002-04-04', [])]
        
        for args in lameVals:
            with self.assertRaises(ValueError):
                self.container.add(Product(*args))

    def testDelete(self):
        # Deleting all elements in a loop 
        for i, p in reversed(list(enumerate(self.testList))):
            self.container.delete(p.getID())
            self.assertEqual(len(self.container), i)
            self.assertNotIn(p, self.lst)

        with self.assertRaises(NameError):
            self.container.delete('LameID')

    def testSort(self):
        # Sorting by all properties in a loop
        for i in range(len((Product.getAttributes()))):    
            self.container.sort(Product.getAttributes()[i])       
            self.testList.sort(key=lambda p: 
                                getattr(p, Product.getGetters()[i])())

            self.assertListEqual(self.lst, self.testList)

        with self.assertRaises(AttributeError):
            self.container.sort('lameAttribute')
        
    def testFind(self):
        found = self.container.find('test')
        self.assertEqual(found._ProductContainer__productList, self.lst)
    
        found = self.container.find('3999')
        self.assertEqual(found, self.lst[1])

        found = self.container.find('01-01')
        self.assertEqual(found, self.lst[0])

        found = self.container.find('.com')
        self.assertEqual(found._ProductContainer__productList, 
                         self.lst[0:2])
    
        found = self.container.find('lameKey')
        empty = ProductContainer()
        self.assertEqual(found._ProductContainer__productList, 
                         empty._ProductContainer__productList)

    def testEdit(self):
        self.container.edit('1', 'title', 'otherTitle') 
        self.assertEqual('otherTitle', self.lst[0].getTitle())

        self.container.edit('2', 'createdAt', '2019-05-05') 
        self.assertEqual('2019-05-05', str(self.lst[1].getCreatedAt()))

        self.container.edit('3', 'imageURL', 'new.url.ua') 
        self.assertEqual('new.url.ua', str(self.lst[2].getImageURL()))

        with self.assertRaises(AttributeError):
            self.container.edit('1', 'lameAtribute', 'otherTitle')

        with self.assertRaises(ValueError):
            self.container.edit('1', 'price', 'lamePrice')
        
        with self.assertRaises(ValueError):
            self.container.edit('1', 'updatedAt', '1800-01-01')

        with self.assertRaises(NameError):
            self.container.edit('lameID', 'price', 'otherTitle')
         
        self.assertEqual('otherTitle', self.lst[0].getTitle())

    def testReadWriteFile(self):
        self.container.writeIntoFile('testProducts.json')
        
        self.container.readFromFile('testProducts.json')
        self.assertEqual(self.testList, self.lst)

    def testUndo(self):
        with self.assertRaises(AttributeError):
            self.caretaker.redo()

        copyList = self.lst.copy()

        for p in testData:
            for _ in range(5):
                self.caretaker.backup()
                self.container.add(p)
                copyList.append(p)
            for _ in range(5):
                self.caretaker.undo()
                copyList.pop()        
                self.assertEqual(self.container._ProductContainer__productList,
                                copyList)

            with self.assertRaises(AttributeError):
                self.caretaker.undo()

    def testRedo(self):
        with self.assertRaises(AttributeError):
            self.caretaker.redo()

        copyList = self.lst.copy()

        for p in testData:
            for _ in range(5):
                self.caretaker.backup()
                self.container.add(p)
            for _ in range(5):
                self.caretaker.undo()
            for _ in range(5):
                self.caretaker.redo()
                copyList.append(p)       
                self.assertEqual(self.container._ProductContainer__productList,
                                copyList)

            with self.assertRaises(AttributeError):
                self.caretaker.redo()     


testData = [Product('testOne', 'test.com.ua', 49.50, '2020-01-01', '2020-04-04', 'test', 1),
            Product('testTwo', 'test.com', 3999.35, '2020-03-03', '2020-04-03', 'test0', 2),
            Product('testThree', 'test.ua', 49.5055, '2020-05-05', '2020-06-06', 'test', 3)]

if __name__ == '__main__':
    unittest.main()