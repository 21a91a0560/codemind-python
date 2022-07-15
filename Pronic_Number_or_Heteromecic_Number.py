n=int(input())
c=0
for i in range(1,n):
  if(n==i*i+1):
   c+=1
   break
if c==1:
    print("NO")
else:
    print("YES")