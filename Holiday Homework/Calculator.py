a = float(input('Enter First Number \n '))
b = float(input('Enter Second Number \n '))
op = input("Enter Oprator ")

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
elif op == '%':
    print(a%b)
else:
    print("INVALID Operator")

