a=int(input())
c=0
t=a
p=a
k=0
while a:
    d=a%10
    c+=1
    a=a//10
while t:
    d=t%10
    k=k+d**c
    c-=1
    t=t//10
if p==k:
  print("True")
else:
    print("False")