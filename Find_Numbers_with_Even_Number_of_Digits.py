n=int(input())
a=list(map(int,input().split()))
p=0
for i in range(0,len(a)):
  c=0
  while a[i]>0:
   d=a[i]%10
   c=c+1
   a[i]=a[i]//10
  if c%2==0:
     p=p+1
print(p)