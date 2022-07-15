s=input()
k=[]
s=s.split()
for i in s:
    k.append(len(i))
print(max(k))