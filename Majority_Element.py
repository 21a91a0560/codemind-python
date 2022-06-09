n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)):
  c=0
  for j in range(0,len(a)):
    if a[i]==a[j] and i!=j:
       c=c+1
  if c>=n//2:
     print(a[i])
     break