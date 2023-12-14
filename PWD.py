import random
print("Welcome to Randome PWD Generator")
randomechars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+"
nbrofpwds = int(input("Please enter the number of Pwd to be Generated: "))
pwdlen = int(input("Please enter the length of Pwd needed: "))

print("Here are your random passwords:")
for x in range(nbrofpwds):
    pwd = ""
    for chars in range(pwdlen):
        pwd = pwd + random.choice(randomechars)
    print(pwd)