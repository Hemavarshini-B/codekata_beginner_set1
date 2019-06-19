num=input().split(" ")
num=map(int,num)
if(num[0]>num[1]):
  if(num[0]>num[2]):
    print(num[0])
  else:
    print(num[2])
elif(num[1]>num[2]):
  print(num[1])
else:
  print(num[2])
