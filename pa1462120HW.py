import random
import numpy as np

"""
(a) Ask the user to input an integer N. Create a list with the length N, containing random numbers between 0 and N*2. Make sure that there are no duplicates in the list created.
(b) Create dictionary N keys, where the keys are the values in the list generated in the previous step. Values are random numbers between 0 and 10.
(c) Create a list that contains the values of the dictionary created in the previous step as its entries.
"""

n = int(input("Enter an integer: "))
newList = []
newDict = {}
otherList = []

for i in range(n):
  x = random.randrange(0,10)
  while(x in newList):
    x = random.randrange(0,10)
  newList.append(x)
  y = random.randrange(0,10)
  while(y in newDict.values()):
    y = random.randrange(0,10)
  newDict[x]=y
  otherList.append(newDict[x])
print(newList)
print(newDict)
print(otherList)

"""
(a)Generate an array with shape (5,1) using the random number generator.
(b)Sort the values in the array in ascending order
"""
a = np.random.randint(-100,100)
b = np.random.randint(-100, 100)
c = np.random.randint(-100, 100)
d = np.random.randint(-100, 100)
e = np.random.randint(-100, 100)
list1 = [[a],[b],[c],[d],[e]]
arr = np.array(list1)
print(arr)
list1.sort()
arr = np.array(list1)
print(arr)