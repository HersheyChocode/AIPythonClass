#Exercise 1


x = int(input("Please enter in an integer from 0 to 10 (inclusive): "))

valid = True
prime = True

if x<0 or x>10:
  print("This is not valid")
  valid = False
else:
  for y in range(2,8):
    if x%y==0 and x!=y:
      print(x, " is not a prime number because it is divisible by ", y)
      prime = False
      break

if prime and valid:
  print("Yes")
 


#Exercise 2
name = input("Please enter your name: ")
print("Nice to meet you, " + str(name) + "!")