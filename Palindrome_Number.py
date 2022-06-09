n=int(input())
for i in range(1,n+1):
  a=int(input())
  temp=a
  r=0
  while a>0:
   d=a%10
   r=r*10+d
   a=a//10
  if r==temp:
     print('True')
  else:
    print('False')