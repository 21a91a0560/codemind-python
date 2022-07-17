n=int(input())
c=list(map(int,input().split()))
a,b=map(int,input().split())
k=0
for i in range(n):
    if c[i]<a or c[i]>b:
        print(c[i],end=' ')
        k=1
if k==0:
    print(-1)
