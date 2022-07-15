n=int(input())
if n==0 or n==1:
 print("True")
else:
    a=0
    b=1
    i=a+b
    while i<n:
        a=b
        b=i
        i=a+b
    if i==n:
        print("True")
    else:
       print("False")