myList=[1,2,3,4,5]
result=[2*item for item in myList]
print(result)

##

myList=[1,2,3,4,5,-4,-6]
result=[4*item for item in myList]
print(result)

##
myList=list(range(100))
filteredItem=[ item for item in myList if item %10==0 ]
print(filteredItem)

##
myList=list(range(100))
filteredItem=[ item for item in myList if item %20==0 ]
print(filteredItem)

myList=list(range(100,1000))
filteredItem=[ item for item in myList if item %50==0 ]
print(filteredItem)

