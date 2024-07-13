n=int(input("Enter a number: "))
l=[]
for i in range (1,n):
    c=0
    if n%i==0:
        for j in range (2,i):
            if j%i==0:
                c+=1
        if c==0:
            l.append(i)
l.sort()
print(l[-1])
