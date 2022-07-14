x=(input())
max=0
k=len(x)
for i in range(0,k):
 if(ord(x[i])>max):
  max=ord(x[i])
print(chr(max))
