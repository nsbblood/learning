# Lets play fizzbuzz

for n in range(1,101):
    if n%15==0:
        print('fizzbuzz')

    else:
        if n%5==0:
            print('Fizz')
        else :
            if n%3==0:
                print('Buzz')
            else:
                print(n)



