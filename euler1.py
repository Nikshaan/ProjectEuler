n=int(input("Enter value of N: "))
sum=0
for i in range(n):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)