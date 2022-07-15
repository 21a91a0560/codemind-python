s=input()
s=s.split()
k=0
for i in s:
    if k%2==0:
        print(i[::-1],end=' ')
    else:
        print(i,end=' ')
    k+=1    

