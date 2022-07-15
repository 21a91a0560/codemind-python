n=int(input())
a=list(map(int,input().split()))
f=0
s=0
for i in range(n//2):
    f=f+a[i]
for i in range(n//2,n):
    s=s+a[i]
print(abs(f-s))        

