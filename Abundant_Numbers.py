n=int(input())
k=0
for i in range(1,(n//2)+1):
    if n%i==0:
        k=k+i
if k>n:
    print("True")
else:
    print("False")