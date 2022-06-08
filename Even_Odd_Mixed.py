n=int(input())
c=0
k=0
m=0
while n>0:
 d=n%10
 c=c+1
 if d%2==0:
    k=k+1
 else:
   m=m+1
 n=n//10
if c==k:
   print('Even')
elif c==m:
  print('Odd')
else:
  print('Mixed')
    