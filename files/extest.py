def factorial(num):
    if type(num)!=int: #we are checking type of the num parameter
        return
    if num <0:
        return
    
    fact =1
    val=1

    while val <=num:
        fact=fact*val
        val=val+1

    return fact #dont forget to return back to fact!!

print(factorial(5))
print(factorial(4))
