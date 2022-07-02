n=int(input())
l=list(map(int,input().strip().split()))
for i in range(n):
    for j in range(i+1,n):
        if l[i]==0:
            t=l[i]
            l[i]=l[j]
            l[j]=t
for i in range(n):
    print(l[i],end=' ')

