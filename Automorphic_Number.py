a=int(input())
c=0
r=0
j=0
p=a
k=a**2
t=a
rev=0
while a:
    d=a%10
    c+=1
    a=a//10
while k:
    d=k%10
    j+=1
    if(j<=c):
     rev=rev*10+d
    k=k//10
while rev:
    d=rev%10
    r=r*10+d
    rev=rev//10
if r==p:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")