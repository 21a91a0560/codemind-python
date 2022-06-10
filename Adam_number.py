n=int(input())
m=n*n
temp=n
r=0
while n>0:
 d=n%10
 r=r*10+d
 n=n//10
k=r*r
org=k
r1=0
while k>0:
 rem=k%10
 r1=r1*10+rem
 k=k//10
if r1==m:
   print('True')
else:
  print('False')