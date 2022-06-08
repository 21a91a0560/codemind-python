def is_prime(k):
 for i in range(2,int(k**0.5)+1):
   if k%i==0:
      return 0
 else:
   return 1
a=int(input())
b=int(input())
n=a+b
k=n+1
s=0
while k>1:
 if is_prime(k):
     s=k
     break
 k=k+1
print(s-n)