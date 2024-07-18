myList=[1,2,3,4]
myList.append(5)
print(myList)

myList.insert(3,'a new value')
print(myList)

myList.insert(2,'here it is')
print(myList)

myList.remove('a new value')
print(myList)

myList.pop()
print(myList)  # It throws latest value (5)

while len(myList):
    print(myList.pop())