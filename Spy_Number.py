x=int(input())
s=0
m=1
while(x!=0):
 d=x%10
 s=s+d
 m=m*d
 x=x//10
if(s==m):
 print("Spy Number")
else:
 print("Not Spy Number")