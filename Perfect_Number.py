n=int(input())
ad=0
for i in range(1,n//2+1):
  if n%i==0:
     ad=ad+i
if ad==n:
   print('True')
else:
   print('False')