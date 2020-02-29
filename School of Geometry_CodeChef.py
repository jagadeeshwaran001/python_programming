#link for problem:-https://www.codechef.com/problems/SNUG_FIT
try:
    t=int(input())
    for i in range(t):
        n=int(input())
        
        a=list(map(int, input().split()))
        b=list(map(int, input().split()))
        
        a=sorted(a)
        b=sorted(b)
        ans=0
        for j in range(n):
            if(a[j]!=b[j]):
                ans=ans+(min(a[j],b[j]))
        print(ans)
except:
    pass
    
