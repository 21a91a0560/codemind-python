n=int(input())
a=list(map(int,input().split()))
c=0
if a[0]==0:
    c+=1
for i in range(1,n):
    if a[i]%2==0 and i%2!=0:
            print("False")
            break
else:
    print("True")