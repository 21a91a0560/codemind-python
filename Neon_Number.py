n=int(input())
t=n*n
r=0
while t:
    d=t%10
    r=r+d
    t//=10
if r==n:
    print("Neon Number")
else:
    print("Not Neon Number")
