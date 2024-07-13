n=int(input("Enter a number: "))
l,ln=[],[]
p,c=1,0
for i in range(n):
    for j in range(n):
        for k in range (n):
            if (i**2)+(j**2)==(k**2) and i<j and j<k and i+j+k==n:
                a=[i,j,k]
                l.append(a)
                c+=1
if c==0:
    print(-1)
else:
    for m in l:
        for q in m:
            p*=q
        ln.append(p)
    ln.sort()
    print(ln[-1])