n=int(input("Enter a number: "))
l=[]
for i in range (100,1000):
    for j in range (100,1000):
        x=i*j
        y=str(x)
        if y==y[::-1] and int(y)<n:
            l.append(int(y))
l.sort()
print(l[-1])
