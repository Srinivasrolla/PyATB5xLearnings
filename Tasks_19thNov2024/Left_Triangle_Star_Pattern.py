#Left Triangle Star Pattern
a=int(input("Enter a positive number :"))
b=a
for i in range(a):
    for j in range(b):
        print('*',end='')
    print()
    b=b-1