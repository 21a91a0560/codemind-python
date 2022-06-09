n=inn=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
  c=0
  for j in range(0,len(a)):
    if a[j]<a[i] and i!=j:
       c=c+1
  print(c,end=' ')