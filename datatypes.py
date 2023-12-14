#DataTypes..

#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType


a = str("Hello World")
print(a)

b = int(20)
print(b)

c = float(20.5)
print(c)

d = complex(1j)	
print(d)

e = list(("apple", "banana", "cherry"))
print(e)

f = tuple(("carrot", "beans", "potato"))		
print(f)

g = range(6)		
print(g)

h = dict(name="John", age=36)		
print(h)

i = set(("red", "orange", "green"))		
print(i)

j = frozenset(("school", "college", "office"))	
print(j)
	
k = bool(5)	
print(k)
	
l = bytes(5)	
print(l)
	
m = bytearray(5)	
print(m)
	
n = memoryview(bytes(5))
print(n)

#print(type(x)) 