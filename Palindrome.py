n=int(input())
rev=0
temp=n
d=0
while temp>0:
 d=temp%10
 rev=rev*10+d
 temp=temp//10
if n==rev:
   print('True')
else:
  print("False")