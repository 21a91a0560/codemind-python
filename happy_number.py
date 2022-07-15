a=int(input())
t=a
r=0
while(t):
    d=t%10
    r=r+(d**2)
    t=t//10
while(r>=10):
    r2=r
    r=0
    while(r2):
        d=r2%10
        r=r+(d**2)
        r2=r2//10
if r==1 or r==7:
    print("True")
else:
    print("False")