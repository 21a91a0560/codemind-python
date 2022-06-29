a=input()
b=input()
ar=[]
br=[]
for i in a:
    if i.isspace():
        continue
    else:
        ar.append(i.lower())
for i in b:
    if i.isspace():
        continue
    else:
        br.append(i.lower())
r=[]
for i in ar:
    if i in br:
        if i not in r:
            r.append(i)
r.sort()
print(len(r))