name = "Hershey"
age = '13.6'

"""

#INT/STRING INITIALIZATION + PRINTING + FORMAT


print(name,age)
print(float(age)+5)

print("I am {0} and I am {1} years old.".format(name,age))

name = input("What is your name? ")
age = input("How old are you? ")

print("Format type is {0}".format(type(age)))

if "." in age:
  age = float(age)
else:
  age = int(age)
"""



"""

#OPERATIONS

nums = input("Enter two numbers seperated by a space: ")
num1 = int(nums.split()[0])
num2 = int(nums.split()[1])


print("Your two numbers added together are: ", num1+num2)
print("Your two numbers subtracted  are: ", num1-num2, " or: ", num2-num1)
print("Your two numbers multiplied together are: ", num1*num2)
print("Your two numbers divided are: ", num1/num2, " or: ", num2/num1)
print("The remainder of when your two numbers are divided is: ", num1%num2, " or: ", num2%num1)
print("Your first number to the power of your second number is: ", num1**num2)
print("Your second number to the power of your first number is: ", num2**num1)
"""


num = input("Please enter a number\n - I will tell you if it is divisible by ten: ")

num = int(num)

if num%10==0:
  print("Yes")
else:
  print("No")
