n=int(input())
m=n*n
ad=0
while m>0:
 d=m%10
 ad=ad+d
 m=m//10
if ad==n:
  print('Neon Number')
else:
  print('Not Neon Number')