n,m=map(int,input().split())
a=list(map(int,input().split()))
l=0
for i in range(n):
    if a[i]<0:
        a[i]=a[i]*(-1)
    c=0
    if a[i]==0:
        c=1
    k=a[i]
    while k:
        d=k%10
        k=k//10
        c+=1
    if m==c:
        l+=1
print(l)        