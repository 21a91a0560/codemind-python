a,b=map(int,input().split())
k=a*b
for i in range(a,k+1):
 if i%a==0 and i%b==0:
     print(i)
     break