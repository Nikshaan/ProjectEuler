n=int(input("Enter the value of n: "))
i,c2=2,0
while c2<n:
    c1=0
    for j in range(2,i):
        if i%j==0:
            c1+=1
    if c1==0:
        c2+=1
    i+=1
print(i-1)
    


