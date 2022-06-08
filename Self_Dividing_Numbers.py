def is_self(n):
  c=0
  k=0
  temp=n
  while n>0:
   d=n%10
   k=k+1
   if d!=0 and temp%d==0:
      c=c+1
   n=n//10
  if k==c:
     return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
  if is_self(i):
     print(i,end=' ')