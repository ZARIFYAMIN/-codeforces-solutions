t=int(input())
while t>0:
   n=int(input())
   a = list(map(int, input().split()))
   c=[]
   flag=True
   for i in range(len(a)):
      if a[i]<n:
         flag=False
         c.append((n-a[i]))
   if flag==True:
      print(0)
   else:
    print(max(c))      
   
   t-=1
