s=input()
s=s.split()
for i in s:
    max=0
    min=999
    for j in i:
        if ord(j)>max:
            max=ord(j)
        if ord(j)<min:
            min=ord(j)
    print(abs(max-min),end=' ')        