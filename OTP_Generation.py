n=input()
s=[]
for i in range(len(n)):
    if int(n[i])%2==0:
        continue
    else:
        s.append(int(n[i])**2)
for i in s:
    print(i,end='')
