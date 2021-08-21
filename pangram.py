a  = 'abcg'
b = [i for i in a]
#print(b)

str1 = 'abc pqr acd'
str2 = [i for i in str1]
#print(str2)

for i in str1:
    for j in b:
        if (i == j):
            #str2.remove(i)
            b.remove(j)
    else:
        print('string is not pangram')
    break
#print(b)
#print(str2)

if len(b) == 0:
    print('string is pangram')
#else:
    #print('string is not pangram')
