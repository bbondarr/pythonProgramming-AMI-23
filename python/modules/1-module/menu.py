import json
from BlablacarBooking import BlablacarBooking
from BlablaList import BlablaList
from Validation import Validation as v


lst = BlablaList()
#fn = input('Enter filename (json/txt): ')
lst.readFromFile('data.json')
print(lst)

file = open('topDriver.txt', mode='w')
file.write(lst.getTopDriver())
file.close()

print(lst.getTopHour())