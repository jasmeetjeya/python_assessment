n=int(input("Enter the Number of rows: "))
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()        

