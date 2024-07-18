def factorial(num):
    if type(num)!=int:
        return
    
    if num<0:
        return
    
    if num==0:
        return 1
    
    return num*factorial(num-1) ## 

print(factorial(4))