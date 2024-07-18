names=['Jack','Lora','Dora','Eli','Cat','Pc']
print(names)

newnames=names.copy()
names.append('Cat')

print(names)
print(newnames)

newnames.remove('Jack')
print(newnames)

newnames.pop()
print(newnames)

newnames.clear()
print(newnames)

