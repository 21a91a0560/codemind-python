n=int(input())
a=list(map(int,input().split()))
k=sum(a)
k=k//n
c=0
for i in range(n):
    if a[i]>=k:
        c+=1
print(c)        
 
