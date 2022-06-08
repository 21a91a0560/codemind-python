def fib(i):
 if i==0:
    return 0
 elif i==1:
    return 1
 else:
    return fib(i-1)+fib(i-2)
n=int(input())
for i in range(0,n):
  print(fib(i),end=' ')