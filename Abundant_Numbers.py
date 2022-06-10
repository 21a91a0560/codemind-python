n=int(input())
add=0
for i in range(1,n//2+1):
  if n%i==0:
     add=add+i
if add>n:
   print('True')
else:
  print('False')