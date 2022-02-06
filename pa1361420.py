#LISTS 

myList = ["mouse", [8,9,10], ['a','b']]

myList1 = []
myList1.append("string")
 

print(myList[0])
print(myList[2][0])

myList = ['apple', 'mango']
myList.append('grapes')

myList1 = [1,2,3,4]
myList1.remove(3)

for fruit in myList:
  print("I Like ", fruit)

for fruit in myList:
  myList1.append(fruit)

print(myList1)


myList = ["apple","grapes","carrots"]
myList.sort()
print(myList)

print("length: ", len(myList))




list1  = ["hello", "hi"]
list2 = ["goodbye", "bye"]

list1.extend(list2)

list3 = list1
print(list3)

morningFoods = ["toast","tea","apples"]

for food in morningFoods:
  print("There was", food, "in breakfast")


#DICTIONARIES

d = {0:10,1:20}
#d.update({2:30})
d[2] = 30
print(d)

d.get