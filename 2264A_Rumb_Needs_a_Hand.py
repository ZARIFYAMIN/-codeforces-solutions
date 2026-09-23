t=int(input())
while t>0:
   flag=True
   n=int(input())
   a = list(map(int, input().split()))
   q=1
   for j in range(len(a)):
      if q!=a[j]:
         flag=False
         break
      else:
          q+=1
 
   if flag==True:
      print("YES")
   else:
      z=1
      ind=[]
      for o in range(len(a)):
            if z!=a[o]:
               ind.append(z-1)
            z+=1
 
      for k in range(len(ind)//2):
         rind1=ind[k]
         rind2=ind[len(ind)-k-1]
         temp=a[rind1]
         a[rind1]=a[rind2]
         a[rind2]=temp
      l=1
      for o in range(len(a)):
            if l!=a[o]:
               flag=True
               print("NO")
               break
            l+=1
      
      if flag==False:
            print("YES")
   t-=1