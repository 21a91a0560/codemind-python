n=int(input())
for i in range(1,n+1):
  m=int(input())
  for j in range(1,m//2+1):
    if j*j==m:
       print('True')
       break
  else:
    print('False')