n=int(input("write the number of rows:"))
for i in range(1,n+1):
    for s in range(n-i):
        print(' ',end='')
    for sta in range(2*i-1):
        print("*",end='')
    print()