try:
    t=int(input())
    for i in range(t):
        nk=list(map(int,input().split()))
        a=list(map(int,input().split()))
        l=list(map(lambda x:x%nk[1],a))
        l=sum(l)
        print(l%nk[1])
except:
    pass