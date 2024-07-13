n=int(input("Enter value of n: "))
j=1
while True:
    c=0
    for i in range(1,(n+1)):
        if j%i==0:
            c+=1
    if c==n:
        print(j)
        break
    else:
        j+=1

