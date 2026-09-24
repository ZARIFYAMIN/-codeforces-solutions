t=int(input())

while t>0:
    n=int(input())
    a=list(map(int, input().split()))
    o=a.count(1)
    z=n-o
    if o>=z:
        print("Bessie")
    else:
        print("Elsie")
    t-=1
