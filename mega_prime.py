def is_prime(n):
  if n==1:
     return 0
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
       return 0
  else:
    return 1
n=int(input())
d=0
pd=0
if is_prime(n):
   while n>0:
    rem=n%10
    d=d+1
    if is_prime(rem):
       pd=pd+1
    n=n//10
   if d==pd:
      print('Mega Prime')
   else:
     print('Not Mega Prime')
else:
  print('Not Mega Prime')