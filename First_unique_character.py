a=input()
c=ind=co=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                c+=1
    if c!=0:
        continue
    else:
        ind=a[i]
        co+=1
        break
if(co!=0):
    print(ind)
else:
    print(-1)