#Exercise 1
x = int(input("Please enter in an integer: "))

valid = True
prime = True

primes = []
for y in range(2,x):
  if x%y==0 and x!=y:
    primes.append(y)
    prime = False
if prime == False:
  print("Your number is not a prime because it is divisble by these following numbers: ")
  for value in primes:
    print(value)

if prime:
  print("Yes")



#Exercise 2
string = str(input("Enter in a string: "))

if len(string)%2 ==0:
  part1 = ""
  part2 = ""
  for letter in range(0,(len(string)//2)):
    part1+=string[letter]
  for letter in range(len(string)//2,len(string)):
    part2+=string[letter]
else:
  part1 = ""
  part2 = ""
  for letter in range(0,(len(string)//2)):
    part1+=string[letter]
  for letter in range(len(string)//2+1,len(string)):
    part2+=string[letter]


if part1==part2:
  print("Yes, it is a palindrome")
else:
  print("No, it is not a palindrome")

if "lol" in string:
  print("I'm laughing out loud")