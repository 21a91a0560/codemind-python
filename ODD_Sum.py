n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,len(a)):
    if a[i]%2==1:
        s=s+a[i]
print(s)