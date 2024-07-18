print(bytes(4))
print(bytes(44))
print(bytes(444))
print(bytes(1))
print(bytes(2))

'''print(bytes('a'))
print(bytes('b')) It gives error as expected. bytes -> 0,1
'''

ebyte=bytearray('😀','utf-8') #bytearray!!
print(f'Here our emojis byte {ebyte}') #chech terminal <3

ebyte[3]=int('89',16)  #we change 4th value of the emoji
print(ebyte.decode('utf-8'))
ebyte[3]=int('87',16)  
print(ebyte.decode('utf-8'))
ebyte[3]=int('88',16)  
print(ebyte.decode('utf-8'))
ebyte[3]=int('84',16)  
print(ebyte.decode('utf-8'))

