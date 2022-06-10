a=int(input())
temp=a
for n in range(a,1,-1):
  for i in range(2,int(a**0.5)+1):
    if n%i==0:
       break
  else:
    p1=n
    break
d1=abs(temp-p1)
while a>1:
 for i in range(2,int(a**0.5)+1):
   if a%i==0:
      break
 else:
   p2=a
   break
 a+=1
d2=abs(temp-p2)
if d1>d2:
   print(d2)
elif d1<d2:
  print(d1)
else:
  print(d1)