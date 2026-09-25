t = int(input())
while t>0:
    #n = int(input())
    a = list(map(int, input().split()))
    b=[]
 
    for i in range(6):
        b.append(min(a))
        a.remove(min(a))
    print(((-1)*sum(b))+sum(a))    
 
    t-=1
    