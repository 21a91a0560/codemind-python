n=int(input())
m=n*n
c=0
org=n
while n>0:
    d=n%10
    c=c+1
    n=n//10
r=0
temp=m
while m>0:
 rem=m%10
 r=r*10+rem
 m=m//10
p=temp%(10**c)
if p==org:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')