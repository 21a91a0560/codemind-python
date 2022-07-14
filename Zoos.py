x=input()
a=len(x)
s=0
c=0
for i in range(0,a):
  if(x[i]=='z'):
     s+=1
  else:
     c+=1
if(c==s*2):     
 print('Yes')
else:
    print("No")