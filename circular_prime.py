def prime(n):
  if n==1:
     return False
  else:
    for i in range(2,n//2+1):
      if n%i==0:
         return False
    else:
      return True
n=int(input())
if prime(n):
   r=0
   while n>0:
    d=n%10
    r=r*10+d
    n=n//10
   if prime(r):
      print('circular prime')
   else:
     print('prime but not a circular prime')
else:
  print('not prime')