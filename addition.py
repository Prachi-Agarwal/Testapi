from os import environ

def adder(**numbers):
  for key, value in numbers.items():
    totalsum = sum(numbers.values())
  print(totalsum)

#adder(a=2, b=3, c=4)
