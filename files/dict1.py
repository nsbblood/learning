carBrands={
    'b':'BMW',
    'a':'Audi',
    'm':'Mustang',
    'me':'Mercedes',
    'T':'Toyota',
}
print(carBrands)

newCars=carBrands.copy()  # Even If you add new cars to carBrands newcars wont be updated
print(f'Here new car brands {newCars}')

newCars.pop('m')
print(f'New cars are updated{newCars}')

'''
newCars.('T', 'Tog')  # How to add new items?
print(newCars)'''

carBrands['n']='Nissan'  #This is how we add new car brands
print(carBrands)

newCars['c']='Citroen'
print(newCars)

newCars.clear()
print(f'latest cars available -> {newCars}')



