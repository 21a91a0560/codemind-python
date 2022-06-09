n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in range(0,len(a)):
  if i%2==0:
     s=s+a[i]
  else:
    c=c+a[i]
if abs(s-c)==0:
   print('YES')
else:
  print('NO')