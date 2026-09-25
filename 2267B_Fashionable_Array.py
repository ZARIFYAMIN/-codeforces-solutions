t = int(input())
while t>0:
    n = int(input())
    a = list(map(int, input().split()))
    cnt={}
    for x in a:
        if x in cnt:
            cnt[x]+=1
        else:
            cnt[x]=1
    ma =max(cnt.values())
    res=[]
    for r in range(1,ma +1):
        val=[]
        for v in cnt:
            if cnt[v]>=r:
                val.append(v)
        val.sort()
        val.reverse()
        for v in val:
            res.append(v)
    an=""
    for v in res:
        an=an+str(v) + " "
    print(an.strip())
 
    t-=1
    