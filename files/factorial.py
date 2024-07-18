def factorial(num):
    if type(num)!=int:
        return
    if num <0:
        return
    
    fact=1 
    counter=1
    while counter <=num:
        fact=fact*counter
        counter=counter+1

    return fact

print(factorial(4))

# First We checked if it is int & if it is bigger than 0
#  