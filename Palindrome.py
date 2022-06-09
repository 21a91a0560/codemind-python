n=int(input())
r=0
temp=n
while n>0:
 d=n%10
 r=r*10+d
 n=n//10
if r==temp:
   print('True')
else:
  print('False')