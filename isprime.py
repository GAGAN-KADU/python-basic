#a = input(int('enter the number to check number is prime or not'))

def isprime(a):
    if a<2:
        return False
        
    elif (a==2) or (a==3):
        return True

    elif (a%2==0) or (a%3==0):
        return False

    for i in range(5,a):
        if (a%i == 0):
            return False
    return True

def next_prime(n):
    while True:
        n+=1
        if isprime(n):
            return n
    return n
n = 14     
if isprime(n):
    print(n,' is prime')
else:
    print(next_prime(n))





