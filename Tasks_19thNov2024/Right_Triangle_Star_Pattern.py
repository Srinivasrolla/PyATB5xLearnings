#Right Triangle Star Pattern
a=int(input("Enter a positive number :"))
for i in range(a):
    for j in range(i+1):
        print("*",end='')
    print()