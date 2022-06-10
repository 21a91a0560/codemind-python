def is_prime(n):
 for i in range(2,int(n**0.5)+1):
   if n%i==0:
      return 0
 else:
   return 1
n=int(input())
c=0
k=0
for i in range(1,n):
  for j in range(1,n):
    if i*j==n:
       if is_prime(i) and is_prime(j):
          print(i,j,end='')
          c=c+1
          break
  if c==1:
     k=k+1
     break
if k==0:
   print('-1')
