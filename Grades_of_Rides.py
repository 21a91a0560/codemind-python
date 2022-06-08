a,b,c=map(int,input().split())
if a>50:
   a=1
if b>60:
   b=1
if c>100:
   c=1
if a==1 and b==1 and c==1:
   print('10')
elif a==1 and b==1:
  print('9')
elif b==1 and c==1:
  print('8')
elif a==1 and c==1:
  print('7')
elif a==1 or b==1 or c==1:
  print('6')
else:
  print('5')