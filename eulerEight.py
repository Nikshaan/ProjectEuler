n=int(input("Enter a number: "))
k=int(input("Enter number of consecutive digits to take: "))

s=str(n)
l=[]
ls=len(s)
while len(s)>=k:
    p=1
    for i in range(k):
        p*=int(s[i])
    l.append(p)
    s=s[1::]

l.sort()
print(l[-1])



