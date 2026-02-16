'''input:4
    output:
    * * * *
    * * * *
    * * * *
    
n=int(input())
for i in range(n):  
    for j in range(n):
        print("*",end=" ")
    print()'''
''' n=4
    *
    * *
    * * *
    * * * * write a program to print the above pattern'''
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''n=4
* * * *
* * *
* *
* '''
n=int(input())
for i in range(n):#for i in range(n,0,-1) for j in range(i)
    for j in range(n-i):#for j in range(i,n)
        print("*",end=" ")
    print()