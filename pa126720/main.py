for i in range(1,5):
  print(i)
  for j in range(1,5):
    print(j)

print("h glaeruhtg;aerh")
for i in range(1,5):
  print(i)
for j in range(1,5):
  print(j)


#Factorial

factorial = 1
n = int(input("Enter a positive integer: "))
for x in range(n,1,-1):
  factorial*=x
print(factorial)


evenNum = int(input("Enter a positive integer: "))

#Writing Files
fileIn = open("file.txt","w")
for x in range(1,evenNum+1):
  if x%2==0:
    fileIn.write(str(x)+"\n")
fileIn.close()
"""
fileIn = open("file.txt","a+")
fileIn.write("\n new appended line")
fileIn.close()
"""

song = ["I","like","to","eat","apples","and","bananas","457","9"]
song.sort()
print(song)