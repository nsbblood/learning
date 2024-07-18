hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
    
    converted = 0
    exponent = len(hexNum) - 1
    
    for char in hexNum:
        converted = converted + (hexNumbers[char] * (16 ** exponent))
        exponent = exponent - 1
        
    return converted

# Testing the function
print(hexToDec('11A'))
print(hexToDec('20A'))
print(hexToDec('30A'))
print(hexToDec('3A')) 
print(len('1abcd'))
print(16**2)
print(hexToDec('3Z')) 
'''
16**2 means 16 raised to the power of 2.
This is the same as multiplying 16 by itself.
The result is 256.
'''