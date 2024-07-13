n=int(input("Enter value of n: "))
diff,sum,sumsq=0,0,0
for i in range(1,(n+1)):
    sum+=i
    sumsq+=(i**2)
diff=(sum**2)-sumsq
print(diff)