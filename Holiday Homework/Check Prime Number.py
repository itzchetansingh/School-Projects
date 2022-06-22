from re import A
from unicodedata import name


n = int(input('Enter a Number \n'))

a = False
if n> 1:
    for i in range(2, n):
        if (n % i) == 0:
            a = True
            break

if a :
    print('It is Not Prime')
else:
    print('It is Prime')