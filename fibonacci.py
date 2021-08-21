list_a = []
a = int(input('enter the range : '))
def fib(n):
    if n == 1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(1,a+1):
    list_a.append(fib(i))

print(list_a)







