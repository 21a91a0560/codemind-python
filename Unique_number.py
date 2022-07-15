n=int(input())
a=0
b=0
c=0
f=0
e=0
i=0
h=0
g=0
j=0
while(n):
    d=n%10
    if d==1:
        a+=1
    if d==2:
        b+=1
    if d==3:
        c+=1
    if d==4:
        f+=1
    if d==5:
        e+=1
    if d==6:
        g+=1
    if d==7:
        h+=1
    if d==8:
        i+=1
    if d==9:
        j+=1
    n=n//10
if  a==2 or h==2 or f==2 or e==2 or b==2 or g==2 or j==2 or i==2 or c==2:
     print("Not Unique Number")
else:
    print("Unique Number")
