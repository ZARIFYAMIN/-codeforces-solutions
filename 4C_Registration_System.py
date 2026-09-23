t=int(input())
di={}
while t>0:
   name=input()
   
   if name in di:
      di[name]+=1
      nname=name+str(di[name])
      print(nname)
   else:
      di[name]=0
      print("OK")
      
   t=t-1