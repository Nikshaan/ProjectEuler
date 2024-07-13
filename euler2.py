n=int(input("Enter value of N: "))
x,y,z=1,2,0
print(x,y, end=" ")
for i in range (3,n+1):
    z=x+y
    x=y
    y=z
    print(z, end=" ")
    