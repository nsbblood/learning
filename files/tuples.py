mySet={'a','b','c'}
print(mySet)

mySet=set(('a','b','c'))
print(mySet)

'''mySet=(('a','b','c')) # this works too but outputs are not exactly same
print(mySet)'''  #You cant use add with this

mySet.add('d')
print(mySet)

if 'a' in mySet:
    print('True a is here')

###

myList= ['a','b','b','c','c','c']
myList=list(set(myList))
print(myList)

print(len(mySet))

##
mySet={'a','b','c'}
mySet.discard('a')
print(mySet)