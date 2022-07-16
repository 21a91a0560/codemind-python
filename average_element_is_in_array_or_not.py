n=int(input())
a=list(map(int,input().split()))
k=sum(a)
f=k//n
if f in a:
    print("True")
else:
    print("False")