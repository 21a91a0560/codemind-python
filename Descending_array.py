n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
b=b[::-1]
if a==b:
    print("yes")
else:
    print("no")

