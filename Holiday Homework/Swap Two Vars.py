a = input('Enter Something For Variable a\n')
b = input('Enter Something For Variable b\n')

print(f'''
Values Before Swap :
In a : {a}
IN b : {b}
''')
a,b =b,a
print(f'''
Values After Swap :
In a : {a}
IN b : {b}
''')