import sys
input = sys.stdin.readline
t=int(input())
 
while t>0:
    n,c=input().split()
    n=int(n)
    s=input().strip()
    co=0
    for i in range(n//2):
        j= n-1-i
        if s[i]==s[j]:
            continue
        elif s[i]==c or s[j]==c:
            co+=1
        else:
            co+=2
    print(co)
    
    t-=1