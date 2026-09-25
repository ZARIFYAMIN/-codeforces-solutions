t=int(input())
while t>0:
   a = list(map(int, input().split()))
   print(max(abs(a[0]-a[1]),abs(a[0]+a[2]-a[1])))         
   t-=1