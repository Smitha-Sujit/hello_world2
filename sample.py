import keyword


print(keyword.kwlist)

def square(num):
    '''Square of a number'''
    return num**2

a= square(2)
print (a)

print(square.__doc__)
k=10
B= id(k)
print(B)

c= hex(id(k))
print(c)

import sys
print(isinstance(c, int))

str1= "hello world"
str2= str1[7]
print(str1[8])
print(str1[:8])
print(str1[8:])
print(str1[:])
print(str1[4:8])
print(str1[2:4:8])
str3= str1.replace('he', 'hi')
print(str1)
print(str3)

str5= "Natural language processing with Python and R and Java"
L= str5.partition("and")
print(L)

C= str5.count("a")
print(C)
str6=" Hello Everyone "
str7=str6.strip()
print(str6)
print(str7)

str7=str6.lstrip()
print(str6)
print(str7)

str7=str6.rstrip()
print(str6)
print(str7)

str6="******Good **********Everyone ******"
str7=str6.lstrip("*")
print(str6)
print(str7)

str7=str6.rstrip("*")
print(str6)
print(str7)

print(str5.startswith("Natural"))
print(str5.endswith("Natural"))

print(str5.split())
print(str5.split("e"))

a=1
b=2
c=3

print("cost of items are {}, {} and {}".format(a,b,c))

print(4+5.7+False)


print(str5.upper())

#print(4+5.7+data)

a=9.7

print(type(a))
print(a)
print(type(int(a)))
print(int(a))
print(type(bool(a)))
print(bool(a))


a=2
b=3
x="Data"
y= "Science"

print(a+b)
print(x+y)
print(a**b) # power
print(a%b)# modullar 
print(a//b)# floor division 

# askey value of characters

from datetime import date

print(date.today())

date1= date(2022, 5, 16)
print(date1)
print(type(date1))
print(date1.isoweekday())

from datetime import datetime as dt
print(dt.now())
date2= dt.now()
print(date2)
print(date2.isoweekday())
print(date2.month)
print(date2.day)