import numpy as np
import random
"""
def print_max(a,b):
  if a > b:
    print(a, ' is maximum')
    return a
  elif a == b:
    print(a, ' is equal to b')
    return(a,b)
  else:
    print(b, ' is maximum')
    return b
"""
def factorial(n):
  product = 1
  for x in range(n):
    product = product*(x+1)
  return product
"""
a = print_max(49857014857014756,56174650871346)
print(a)

def min_max(list_example):
  min_value = min(list_example)
  max_value = max(list_example)
  return min_value, max_value

print(min_max([134135426363,345245,46332,45246,23135]))


list_2d = [[1,2,3,4],
           [5,2,4,2],
           [1,2,0,1]]

arr = np.array(list_2d)

print(arr)

list_2d = [[1,'fg',3,4],
           [5,2,4,2],
           [1,2,0,1]]

arr = np.array(list_2d)

print(arr)
"""
print(factorial(5))
name = ["Aarav","Anay","Arhana","Arya","Harshini","Jayanth","Kevin","Rahul","Sophia","Anil"]

print(name[random.randint(0,8)])