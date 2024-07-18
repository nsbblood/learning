myList=list(range(100))
filteredList=[item for item in myList if item%10<3]
print(filteredList)

myList=list(range(100))
filteredList=[item for item in myList if item%10>8]
print(filteredList)

myList=list(range(500,750))
filteredList=[item for item in myList if item%19>8]
print(filteredList)

