def fact(n):
  p=1
  for i in range(1,n+1):
    p=p*i
  return p
n=int(input())
ad=0
temp=n
while n>0:
 d=n%10
 k=fact(d)
 ad=ad+k
 n=n//10
if ad==temp:
   print('The number',temp,'is a strong number')
else:
  print('The number',temp,'is not a strong number')