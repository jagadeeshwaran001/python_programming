#link for problem:-https://www.codechef.com/submit/ZUBTRCNT
try:
    t=int(input())
    s=[]
    for i in range(t):
        l,k=map(int,input().split())
        if(l!=k and l>k):
            l=l+1
            l=l-k
            s.append(int((l*(l+1))/2))
        elif(l==k):
            s.append("1")
        elif(l<k):
            s.append("0")
    for i in range(0,len(s)):
        print("Case "+str(i+1)+": "+str(s[i]))
except:
    pass