a = int(input('Till What index '))
b = [0,1]
i = 0
while i < a :
    x = b[0]+b[1]
    print(b[0]+b[1],end=',')
    b[0] = b[1]
    b[1] = x
    i = i+1