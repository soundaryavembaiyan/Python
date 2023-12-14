#Variable Declaration & Type
x = 5
y = "Emir Tahrun"
print('Variable Declaration & Type:')
print('Type of x is:',type(x)) #shows its type
print('Name is:',y)

#Multiple Values..

x, y, z = "Orange", "Banana", "Cherry"
print('Multiple Values:')
print('x',x)
print('y',y)
print('z',z)

#One value to Multiple Variables..

x = y = z = "Orange"
print('One value to Multiple Variables:')
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits

print(a)
print(b)
print(c)


# '+' operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Global Variable
x = "awesoming"
def myfunc():
  global x
  x = "Good"
  print("Py is gg" + x)
  
  f = "fantastic"
  print("Python is fff" + f)

myfunc()

def Zfunc():
 print("Python is aww " + x)


