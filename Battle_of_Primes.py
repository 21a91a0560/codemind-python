a=int(input())
b=int(input())
n=a+b
org=n
temp=n+1
while n>0:
 for i in range(2,int(temp**0.5)+1):
   if temp%i==0:
      break;
 else:
   k=temp
   break
 temp=temp+1
print(abs(k-org))
