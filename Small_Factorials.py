n=int(input())
s=1
for i in range(1,n+1):
  m=int(input())
  for j in range(1,m+1):
    s=s*j
  print(s)
  s=1