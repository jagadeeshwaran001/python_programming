#link for the problem:-https://www.codechef.com/problems/CHPINTU
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    f=list(map(int,input().split()))
    p=list(map(int,input().split()))
    s=list(set(f))
    l=[]
    for i in range(len(s)):
        su=0
        for j in range(len(f)):
            if(s[i]==f[j]):
                su=su+p[j]
        l.append(su)
    print(min(l))
                