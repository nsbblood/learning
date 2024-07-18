a=[1,2,3,4,5,6]
b=a
a.append(7)
print(b)

##
a=[1,2,3,4,5,6]
b=a.copy()  #This way if something is added to a then b wont be changed
a.append(7)
print(a)
print(b)

##
a=[1,2,3,4,5,6]
b=a
c=b
a.append(7)
b.append(100)
print(a)
print(b)
print(c)

##
a=[1,2,3,4,5,6]
b=a.copy()
c=b.copy()
a.append(7)
b.append(100)
print(a)
print(b)
print(c)