import sys


def add(a,b):
  return ("value of addition : " + str(a+b))
# result=add(10,20)
# print(result)


def sub(a,b):
  return ("value of subtraction : " + str(a-b))
# result=sub(10,20)

# passing input from command line 

a= float(sys.argv[1])
operation=sys.argv[2]
b= float(sys.argv[3])

if operation=="add":
  output=add(a,b)
  print(output)


if operation=="sub":
  output=sub(a,b)
  print(output)
