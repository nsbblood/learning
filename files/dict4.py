animals={
    'b': ['bison'],
    'c':['cat'],
    'd': ['dog'],

}

animals['e']=['ewww']

print(animals)

##
if 'k' not in animals:       
    animals['k']=[]

animals['k'].append('Koala')
print(animals)

