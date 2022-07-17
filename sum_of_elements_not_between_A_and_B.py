n=int(input())
a=list(map(int,input().split()))
k,m=map(int,input().split())
s=0
for i in range(n):
    if a[i]<k or a[i]>m:
        s=s+a[i]
print(s)        