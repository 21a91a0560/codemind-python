n=int(input())
a=list(map(int,input().split()))
k,m=map(int,input().split())
s=[]
f=0
for i in range(n):
    if a[i]<k or a[i]>m:
        s.append(a[i])
        f=1
if f==0:
    print(-1)
else:
    print(max(s))        