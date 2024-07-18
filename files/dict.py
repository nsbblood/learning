animals = {
    'b': 'bird',
    'c': 'cat',
    'm': 'monkey',
}
print(animals)

newanim=animals.copy()

newanim.pop('m') # you remove monkey...
print(newanim)
