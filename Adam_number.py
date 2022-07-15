a=int(input())
s=a**2
r=0
while a:
    d=a%10
    r=r*10+d
    a=a//10
s1=r**2
r1=0
while s1:
    d=s1%10
    r1=r1*10+d
    s1=s1//10
if s==r1:
    print("True")
else:
    print("False")