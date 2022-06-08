def is_sum(n):
    s=0
    while n:
        d=n%10
        s=s+d
        n=n//10
    if s<=9:
        return s
    else:
        n=is_sum(s)
        return n
n=int(input())
print(is_sum(n))