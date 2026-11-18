n = int(input("Length of pattern : "))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("@",end=" ")
    for j in range(n):
        print("@",end=" ")
    for j in range(i+1):
        print("@",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("@",end=" ")
    for j in range(n):
        print("@",end=" ")
    for j in range(i+1):
        print("@",end=" ")
    print()                         
for i in range(n):
    for j in range(n*6+4):
        print("@",end=" ")
    print()
for i in range(n*3+2):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n*3+1):
        print("@",end=" ")
    for j in range(i,n*3+1):
        print("@",end=" ")
    print()        

