n=int(input())
c=0
for i in range(1,n+1):
  if n%i==0:
     if i==1:
         c=1
     else:
       for j in range(2,i//2+1):
         if i%j==0:
             c=c+1
             break
print(c)