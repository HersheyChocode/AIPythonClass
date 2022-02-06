#Exercise 1
List1 = ["batman", "superman", "aquaman", "flash", "arrow"]
List2 = ["batmobile", "cape", "glove", "lightning", "bow"]
for x in range(len(List1)):
  print("In my collection, I have", List1[x])
for x in range(len(List1)):
  print(List1[x], "has", List2[x])

#Exercise 2
numDict = {1: 10, 2: 20}
mixed_Dict = {'Red Sox': 'Boston', '3': 'Sandy Leon', }

newDict = {'Red Sox': 'Boston', 1:10, '3': 'Sandy Leon',2: 20}

for key in newDict:
  print("The key is", key, "the value is", newDict[key])

for key in newDict:
  print("The key is", key,"and it is inside the dictionary")
  otherDict = {key: newDict[key]}
  print(otherDict) 