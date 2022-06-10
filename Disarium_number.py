n=int(input())
c=0
temp=n
m=n
r=0
while n>0:
 d=n%10
 c=c+1
 n=n//10
 s=0
while m>0:
 rem=m%10
 s=s+(rem**c)
 m=m//10
 c=c-1
if s==temp:
   print('True')
else:
  print('False')