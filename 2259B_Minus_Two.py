import sys
input= sys.stdin.readline
 
t=int(input())
 
while t>0:
   odd=0
   st=0
   g1=0
   g2=0
   n=int(input())
   a=list(map(int,input().split())) 
   for i in range(n):
      if a[i]%2!=0:
            odd+=1
      else:
            s=a[i]//2
            if s%2==0:
                g1+=1
            else:
                g2+=1
 
 
   print(max(odd,g1,g2))
   t=t-1
 