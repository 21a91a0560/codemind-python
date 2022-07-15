s=input()
s=s.lower()
a='aeiou'
k=0
m=0
for i in s:
    if i in a:
       m=1
       k+=1
if m==0:
    print(0)
else:
 print(k)
       