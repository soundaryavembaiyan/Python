a = "Hello"
print(a)

#slicing str
b = "Hello, World!"
print(b[2:5])

#Upper nd Lower case
u = "Hello, World!"
print(u.upper())

l = "Hello, World!"
print(l.lower())

#concardination
a = "Hellooooo"
b = "Wooooorld"
c = a + " " + b
print(c)


#Format strs
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

#Escape char.
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 